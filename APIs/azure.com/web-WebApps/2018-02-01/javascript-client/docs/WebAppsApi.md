# WebAppsApiClient.WebAppsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webAppsAddPremierAddOn**](WebAppsApi.md#webAppsAddPremierAddOn) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons/{premierAddOnName} | Updates a named add-on of an app.
[**webAppsAddPremierAddOnSlot**](WebAppsApi.md#webAppsAddPremierAddOnSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premierAddOnName} | Updates a named add-on of an app.
[**webAppsAnalyzeCustomHostname**](WebAppsApi.md#webAppsAnalyzeCustomHostname) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/analyzeCustomHostname | Analyze a custom hostname.
[**webAppsAnalyzeCustomHostnameSlot**](WebAppsApi.md#webAppsAnalyzeCustomHostnameSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/analyzeCustomHostname | Analyze a custom hostname.
[**webAppsApplySlotConfigToProduction**](WebAppsApi.md#webAppsApplySlotConfigToProduction) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/applySlotConfig | Applies the configuration settings from the target slot onto the current slot.
[**webAppsApplySlotConfigurationSlot**](WebAppsApi.md#webAppsApplySlotConfigurationSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/applySlotConfig | Applies the configuration settings from the target slot onto the current slot.
[**webAppsBackup**](WebAppsApi.md#webAppsBackup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backup | Creates a backup of an app.
[**webAppsBackupSlot**](WebAppsApi.md#webAppsBackupSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backup | Creates a backup of an app.
[**webAppsCreateDeployment**](WebAppsApi.md#webAppsCreateDeployment) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/deployments/{id} | Create a deployment for an app, or a deployment slot.
[**webAppsCreateDeploymentSlot**](WebAppsApi.md#webAppsCreateDeploymentSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id} | Create a deployment for an app, or a deployment slot.
[**webAppsCreateFunction**](WebAppsApi.md#webAppsCreateFunction) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/functions/{functionName} | Create function for web site, or a deployment slot.
[**webAppsCreateInstanceFunctionSlot**](WebAppsApi.md#webAppsCreateInstanceFunctionSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/{functionName} | Create function for web site, or a deployment slot.
[**webAppsCreateInstanceMSDeployOperation**](WebAppsApi.md#webAppsCreateInstanceMSDeployOperation) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/extensions/MSDeploy | Invoke the MSDeploy web app extension.
[**webAppsCreateInstanceMSDeployOperationSlot**](WebAppsApi.md#webAppsCreateInstanceMSDeployOperationSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/extensions/MSDeploy | Invoke the MSDeploy web app extension.
[**webAppsCreateMSDeployOperation**](WebAppsApi.md#webAppsCreateMSDeployOperation) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/extensions/MSDeploy | Invoke the MSDeploy web app extension.
[**webAppsCreateMSDeployOperationSlot**](WebAppsApi.md#webAppsCreateMSDeployOperationSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/extensions/MSDeploy | Invoke the MSDeploy web app extension.
[**webAppsCreateOrUpdate**](WebAppsApi.md#webAppsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name} | Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.
[**webAppsCreateOrUpdateConfiguration**](WebAppsApi.md#webAppsCreateOrUpdateConfiguration) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/web | Updates the configuration of an app.
[**webAppsCreateOrUpdateConfigurationSlot**](WebAppsApi.md#webAppsCreateOrUpdateConfigurationSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web | Updates the configuration of an app.
[**webAppsCreateOrUpdateDomainOwnershipIdentifier**](WebAppsApi.md#webAppsCreateOrUpdateDomainOwnershipIdentifier) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/domainOwnershipIdentifiers/{domainOwnershipIdentifierName} | Creates a domain ownership identifier for web app, or updates an existing ownership identifier.
[**webAppsCreateOrUpdateDomainOwnershipIdentifierSlot**](WebAppsApi.md#webAppsCreateOrUpdateDomainOwnershipIdentifierSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/domainOwnershipIdentifiers/{domainOwnershipIdentifierName} | Creates a domain ownership identifier for web app, or updates an existing ownership identifier.
[**webAppsCreateOrUpdateFunctionSecret**](WebAppsApi.md#webAppsCreateOrUpdateFunctionSecret) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/functions/{functionName}/keys/{keyName} | Add or update a function secret.
[**webAppsCreateOrUpdateFunctionSecretSlot**](WebAppsApi.md#webAppsCreateOrUpdateFunctionSecretSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/{functionName}/keys/{keyName} | Add or update a function secret.
[**webAppsCreateOrUpdateHostNameBinding**](WebAppsApi.md#webAppsCreateOrUpdateHostNameBinding) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{hostName} | Creates a hostname binding for an app.
[**webAppsCreateOrUpdateHostNameBindingSlot**](WebAppsApi.md#webAppsCreateOrUpdateHostNameBindingSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{hostName} | Creates a hostname binding for an app.
[**webAppsCreateOrUpdateHostSecret**](WebAppsApi.md#webAppsCreateOrUpdateHostSecret) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/host/default/{keyType}/{keyName} | Add or update a host level secret.
[**webAppsCreateOrUpdateHostSecretSlot**](WebAppsApi.md#webAppsCreateOrUpdateHostSecretSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/host/default/{keyType}/{keyName} | Add or update a host level secret.
[**webAppsCreateOrUpdateHybridConnection**](WebAppsApi.md#webAppsCreateOrUpdateHybridConnection) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName} | Creates a new Hybrid Connection using a Service Bus relay.
[**webAppsCreateOrUpdateHybridConnectionSlot**](WebAppsApi.md#webAppsCreateOrUpdateHybridConnectionSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName} | Creates a new Hybrid Connection using a Service Bus relay.
[**webAppsCreateOrUpdatePublicCertificate**](WebAppsApi.md#webAppsCreateOrUpdatePublicCertificate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/publicCertificates/{publicCertificateName} | Creates a hostname binding for an app.
[**webAppsCreateOrUpdatePublicCertificateSlot**](WebAppsApi.md#webAppsCreateOrUpdatePublicCertificateSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/publicCertificates/{publicCertificateName} | Creates a hostname binding for an app.
[**webAppsCreateOrUpdateRelayServiceConnection**](WebAppsApi.md#webAppsCreateOrUpdateRelayServiceConnection) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entityName} | Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).
[**webAppsCreateOrUpdateRelayServiceConnectionSlot**](WebAppsApi.md#webAppsCreateOrUpdateRelayServiceConnectionSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entityName} | Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).
[**webAppsCreateOrUpdateSlot**](WebAppsApi.md#webAppsCreateOrUpdateSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot} | Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.
[**webAppsCreateOrUpdateSourceControl**](WebAppsApi.md#webAppsCreateOrUpdateSourceControl) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web | Updates the source control configuration of an app.
[**webAppsCreateOrUpdateSourceControlSlot**](WebAppsApi.md#webAppsCreateOrUpdateSourceControlSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web | Updates the source control configuration of an app.
[**webAppsCreateOrUpdateSwiftVirtualNetworkConnection**](WebAppsApi.md#webAppsCreateOrUpdateSwiftVirtualNetworkConnection) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/networkConfig/virtualNetwork | Integrates this Web App with a Virtual Network. This requires that 1) \&quot;swiftSupported\&quot; is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not  in use by another App Service Plan other than the one this App is in.
[**webAppsCreateOrUpdateSwiftVirtualNetworkConnectionSlot**](WebAppsApi.md#webAppsCreateOrUpdateSwiftVirtualNetworkConnectionSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkConfig/virtualNetwork | Integrates this Web App with a Virtual Network. This requires that 1) \&quot;swiftSupported\&quot; is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not  in use by another App Service Plan other than the one this App is in.
[**webAppsCreateOrUpdateVnetConnection**](WebAppsApi.md#webAppsCreateOrUpdateVnetConnection) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName} | Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).
[**webAppsCreateOrUpdateVnetConnectionGateway**](WebAppsApi.md#webAppsCreateOrUpdateVnetConnectionGateway) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).
[**webAppsCreateOrUpdateVnetConnectionGatewaySlot**](WebAppsApi.md#webAppsCreateOrUpdateVnetConnectionGatewaySlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).
[**webAppsCreateOrUpdateVnetConnectionSlot**](WebAppsApi.md#webAppsCreateOrUpdateVnetConnectionSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName} | Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).
[**webAppsDelete**](WebAppsApi.md#webAppsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name} | Deletes a web, mobile, or API app, or one of the deployment slots.
[**webAppsDeleteBackup**](WebAppsApi.md#webAppsDeleteBackup) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups/{backupId} | Deletes a backup of an app by its ID.
[**webAppsDeleteBackupConfiguration**](WebAppsApi.md#webAppsDeleteBackupConfiguration) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/backup | Deletes the backup configuration of an app.
[**webAppsDeleteBackupConfigurationSlot**](WebAppsApi.md#webAppsDeleteBackupConfigurationSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/backup | Deletes the backup configuration of an app.
[**webAppsDeleteBackupSlot**](WebAppsApi.md#webAppsDeleteBackupSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backupId} | Deletes a backup of an app by its ID.
[**webAppsDeleteContinuousWebJob**](WebAppsApi.md#webAppsDeleteContinuousWebJob) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/continuouswebjobs/{webJobName} | Delete a continuous web job by its ID for an app, or a deployment slot.
[**webAppsDeleteContinuousWebJobSlot**](WebAppsApi.md#webAppsDeleteContinuousWebJobSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/continuouswebjobs/{webJobName} | Delete a continuous web job by its ID for an app, or a deployment slot.
[**webAppsDeleteDeployment**](WebAppsApi.md#webAppsDeleteDeployment) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/deployments/{id} | Delete a deployment by its ID for an app, or a deployment slot.
[**webAppsDeleteDeploymentSlot**](WebAppsApi.md#webAppsDeleteDeploymentSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id} | Delete a deployment by its ID for an app, or a deployment slot.
[**webAppsDeleteDomainOwnershipIdentifier**](WebAppsApi.md#webAppsDeleteDomainOwnershipIdentifier) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/domainOwnershipIdentifiers/{domainOwnershipIdentifierName} | Deletes a domain ownership identifier for a web app.
[**webAppsDeleteDomainOwnershipIdentifierSlot**](WebAppsApi.md#webAppsDeleteDomainOwnershipIdentifierSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/domainOwnershipIdentifiers/{domainOwnershipIdentifierName} | Deletes a domain ownership identifier for a web app.
[**webAppsDeleteFunction**](WebAppsApi.md#webAppsDeleteFunction) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/functions/{functionName} | Delete a function for web site, or a deployment slot.
[**webAppsDeleteFunctionSecret**](WebAppsApi.md#webAppsDeleteFunctionSecret) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/functions/{functionName}/keys/{keyName} | Delete a function secret.
[**webAppsDeleteFunctionSecretSlot**](WebAppsApi.md#webAppsDeleteFunctionSecretSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/{functionName}/keys/{keyName} | Delete a function secret.
[**webAppsDeleteHostNameBinding**](WebAppsApi.md#webAppsDeleteHostNameBinding) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{hostName} | Deletes a hostname binding for an app.
[**webAppsDeleteHostNameBindingSlot**](WebAppsApi.md#webAppsDeleteHostNameBindingSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{hostName} | Deletes a hostname binding for an app.
[**webAppsDeleteHostSecret**](WebAppsApi.md#webAppsDeleteHostSecret) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/host/default/{keyType}/{keyName} | Delete a host level secret.
[**webAppsDeleteHostSecretSlot**](WebAppsApi.md#webAppsDeleteHostSecretSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/host/default/{keyType}/{keyName} | Delete a host level secret.
[**webAppsDeleteHybridConnection**](WebAppsApi.md#webAppsDeleteHybridConnection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName} | Removes a Hybrid Connection from this site.
[**webAppsDeleteHybridConnectionSlot**](WebAppsApi.md#webAppsDeleteHybridConnectionSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName} | Removes a Hybrid Connection from this site.
[**webAppsDeleteInstanceFunctionSlot**](WebAppsApi.md#webAppsDeleteInstanceFunctionSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/{functionName} | Delete a function for web site, or a deployment slot.
[**webAppsDeleteInstanceProcess**](WebAppsApi.md#webAppsDeleteInstanceProcess) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/processes/{processId} | Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.
[**webAppsDeleteInstanceProcessSlot**](WebAppsApi.md#webAppsDeleteInstanceProcessSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/processes/{processId} | Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.
[**webAppsDeletePremierAddOn**](WebAppsApi.md#webAppsDeletePremierAddOn) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons/{premierAddOnName} | Delete a premier add-on from an app.
[**webAppsDeletePremierAddOnSlot**](WebAppsApi.md#webAppsDeletePremierAddOnSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premierAddOnName} | Delete a premier add-on from an app.
[**webAppsDeleteProcess**](WebAppsApi.md#webAppsDeleteProcess) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/processes/{processId} | Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.
[**webAppsDeleteProcessSlot**](WebAppsApi.md#webAppsDeleteProcessSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes/{processId} | Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.
[**webAppsDeletePublicCertificate**](WebAppsApi.md#webAppsDeletePublicCertificate) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/publicCertificates/{publicCertificateName} | Deletes a hostname binding for an app.
[**webAppsDeletePublicCertificateSlot**](WebAppsApi.md#webAppsDeletePublicCertificateSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/publicCertificates/{publicCertificateName} | Deletes a hostname binding for an app.
[**webAppsDeleteRelayServiceConnection**](WebAppsApi.md#webAppsDeleteRelayServiceConnection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entityName} | Deletes a relay service connection by its name.
[**webAppsDeleteRelayServiceConnectionSlot**](WebAppsApi.md#webAppsDeleteRelayServiceConnectionSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entityName} | Deletes a relay service connection by its name.
[**webAppsDeleteSiteExtension**](WebAppsApi.md#webAppsDeleteSiteExtension) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/siteextensions/{siteExtensionId} | Remove a site extension from a web site, or a deployment slot.
[**webAppsDeleteSiteExtensionSlot**](WebAppsApi.md#webAppsDeleteSiteExtensionSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/siteextensions/{siteExtensionId} | Remove a site extension from a web site, or a deployment slot.
[**webAppsDeleteSlot**](WebAppsApi.md#webAppsDeleteSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot} | Deletes a web, mobile, or API app, or one of the deployment slots.
[**webAppsDeleteSourceControl**](WebAppsApi.md#webAppsDeleteSourceControl) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web | Deletes the source control configuration of an app.
[**webAppsDeleteSourceControlSlot**](WebAppsApi.md#webAppsDeleteSourceControlSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web | Deletes the source control configuration of an app.
[**webAppsDeleteSwiftVirtualNetwork**](WebAppsApi.md#webAppsDeleteSwiftVirtualNetwork) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/networkConfig/virtualNetwork | Deletes a Swift Virtual Network connection from an app (or deployment slot).
[**webAppsDeleteSwiftVirtualNetworkSlot**](WebAppsApi.md#webAppsDeleteSwiftVirtualNetworkSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkConfig/virtualNetwork | Deletes a Swift Virtual Network connection from an app (or deployment slot).
[**webAppsDeleteTriggeredWebJob**](WebAppsApi.md#webAppsDeleteTriggeredWebJob) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/triggeredwebjobs/{webJobName} | Delete a triggered web job by its ID for an app, or a deployment slot.
[**webAppsDeleteTriggeredWebJobSlot**](WebAppsApi.md#webAppsDeleteTriggeredWebJobSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/triggeredwebjobs/{webJobName} | Delete a triggered web job by its ID for an app, or a deployment slot.
[**webAppsDeleteVnetConnection**](WebAppsApi.md#webAppsDeleteVnetConnection) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName} | Deletes a connection from an app (or deployment slot to a named virtual network.
[**webAppsDeleteVnetConnectionSlot**](WebAppsApi.md#webAppsDeleteVnetConnectionSlot) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName} | Deletes a connection from an app (or deployment slot to a named virtual network.
[**webAppsDiscoverBackup**](WebAppsApi.md#webAppsDiscoverBackup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/discoverbackup | Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup.
[**webAppsDiscoverBackupSlot**](WebAppsApi.md#webAppsDiscoverBackupSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/discoverbackup | Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup.
[**webAppsGenerateNewSitePublishingPassword**](WebAppsApi.md#webAppsGenerateNewSitePublishingPassword) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/newpassword | Generates a new publishing password for an app (or deployment slot, if specified).
[**webAppsGenerateNewSitePublishingPasswordSlot**](WebAppsApi.md#webAppsGenerateNewSitePublishingPasswordSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/newpassword | Generates a new publishing password for an app (or deployment slot, if specified).
[**webAppsGet**](WebAppsApi.md#webAppsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name} | Gets the details of a web, mobile, or API app.
[**webAppsGetAuthSettings**](WebAppsApi.md#webAppsGetAuthSettings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/authsettings/list | Gets the Authentication/Authorization settings of an app.
[**webAppsGetAuthSettingsSlot**](WebAppsApi.md#webAppsGetAuthSettingsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/authsettings/list | Gets the Authentication/Authorization settings of an app.
[**webAppsGetBackupConfiguration**](WebAppsApi.md#webAppsGetBackupConfiguration) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/backup/list | Gets the backup configuration of an app.
[**webAppsGetBackupConfigurationSlot**](WebAppsApi.md#webAppsGetBackupConfigurationSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/backup/list | Gets the backup configuration of an app.
[**webAppsGetBackupStatus**](WebAppsApi.md#webAppsGetBackupStatus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups/{backupId} | Gets a backup of an app by its ID.
[**webAppsGetBackupStatusSlot**](WebAppsApi.md#webAppsGetBackupStatusSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backupId} | Gets a backup of an app by its ID.
[**webAppsGetConfiguration**](WebAppsApi.md#webAppsGetConfiguration) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/web | Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.
[**webAppsGetConfigurationSlot**](WebAppsApi.md#webAppsGetConfigurationSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web | Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.
[**webAppsGetConfigurationSnapshot**](WebAppsApi.md#webAppsGetConfigurationSnapshot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/web/snapshots/{snapshotId} | Gets a snapshot of the configuration of an app at a previous point in time.
[**webAppsGetConfigurationSnapshotSlot**](WebAppsApi.md#webAppsGetConfigurationSnapshotSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web/snapshots/{snapshotId} | Gets a snapshot of the configuration of an app at a previous point in time.
[**webAppsGetContainerLogsZip**](WebAppsApi.md#webAppsGetContainerLogsZip) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/containerlogs/zip/download | Gets the ZIP archived docker log files for the given site
[**webAppsGetContainerLogsZipSlot**](WebAppsApi.md#webAppsGetContainerLogsZipSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/containerlogs/zip/download | Gets the ZIP archived docker log files for the given site
[**webAppsGetContinuousWebJob**](WebAppsApi.md#webAppsGetContinuousWebJob) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/continuouswebjobs/{webJobName} | Gets a continuous web job by its ID for an app, or a deployment slot.
[**webAppsGetContinuousWebJobSlot**](WebAppsApi.md#webAppsGetContinuousWebJobSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/continuouswebjobs/{webJobName} | Gets a continuous web job by its ID for an app, or a deployment slot.
[**webAppsGetDeployment**](WebAppsApi.md#webAppsGetDeployment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/deployments/{id} | Get a deployment by its ID for an app, or a deployment slot.
[**webAppsGetDeploymentSlot**](WebAppsApi.md#webAppsGetDeploymentSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id} | Get a deployment by its ID for an app, or a deployment slot.
[**webAppsGetDiagnosticLogsConfiguration**](WebAppsApi.md#webAppsGetDiagnosticLogsConfiguration) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/logs | Gets the logging configuration of an app.
[**webAppsGetDiagnosticLogsConfigurationSlot**](WebAppsApi.md#webAppsGetDiagnosticLogsConfigurationSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/logs | Gets the logging configuration of an app.
[**webAppsGetDomainOwnershipIdentifier**](WebAppsApi.md#webAppsGetDomainOwnershipIdentifier) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/domainOwnershipIdentifiers/{domainOwnershipIdentifierName} | Get domain ownership identifier for web app.
[**webAppsGetDomainOwnershipIdentifierSlot**](WebAppsApi.md#webAppsGetDomainOwnershipIdentifierSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/domainOwnershipIdentifiers/{domainOwnershipIdentifierName} | Get domain ownership identifier for web app.
[**webAppsGetFunction**](WebAppsApi.md#webAppsGetFunction) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/functions/{functionName} | Get function information by its ID for web site, or a deployment slot.
[**webAppsGetFunctionsAdminToken**](WebAppsApi.md#webAppsGetFunctionsAdminToken) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/functions/admin/token | Fetch a short lived token that can be exchanged for a master key.
[**webAppsGetFunctionsAdminTokenSlot**](WebAppsApi.md#webAppsGetFunctionsAdminTokenSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/admin/token | Fetch a short lived token that can be exchanged for a master key.
[**webAppsGetHostNameBinding**](WebAppsApi.md#webAppsGetHostNameBinding) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostNameBindings/{hostName} | Get the named hostname binding for an app (or deployment slot, if specified).
[**webAppsGetHostNameBindingSlot**](WebAppsApi.md#webAppsGetHostNameBindingSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings/{hostName} | Get the named hostname binding for an app (or deployment slot, if specified).
[**webAppsGetHybridConnection**](WebAppsApi.md#webAppsGetHybridConnection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName} | Retrieves a specific Service Bus Hybrid Connection used by this Web App.
[**webAppsGetHybridConnectionSlot**](WebAppsApi.md#webAppsGetHybridConnectionSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName} | Retrieves a specific Service Bus Hybrid Connection used by this Web App.
[**webAppsGetInstanceFunctionSlot**](WebAppsApi.md#webAppsGetInstanceFunctionSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/{functionName} | Get function information by its ID for web site, or a deployment slot.
[**webAppsGetInstanceMSDeployLog**](WebAppsApi.md#webAppsGetInstanceMSDeployLog) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/extensions/MSDeploy/log | Get the MSDeploy Log for the last MSDeploy operation.
[**webAppsGetInstanceMSDeployLogSlot**](WebAppsApi.md#webAppsGetInstanceMSDeployLogSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/extensions/MSDeploy/log | Get the MSDeploy Log for the last MSDeploy operation.
[**webAppsGetInstanceMsDeployStatus**](WebAppsApi.md#webAppsGetInstanceMsDeployStatus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/extensions/MSDeploy | Get the status of the last MSDeploy operation.
[**webAppsGetInstanceMsDeployStatusSlot**](WebAppsApi.md#webAppsGetInstanceMsDeployStatusSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/extensions/MSDeploy | Get the status of the last MSDeploy operation.
[**webAppsGetInstanceProcess**](WebAppsApi.md#webAppsGetInstanceProcess) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/processes/{processId} | Get process information by its ID for a specific scaled-out instance in a web site.
[**webAppsGetInstanceProcessDump**](WebAppsApi.md#webAppsGetInstanceProcessDump) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/processes/{processId}/dump | Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.
[**webAppsGetInstanceProcessDumpSlot**](WebAppsApi.md#webAppsGetInstanceProcessDumpSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/processes/{processId}/dump | Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.
[**webAppsGetInstanceProcessModule**](WebAppsApi.md#webAppsGetInstanceProcessModule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/processes/{processId}/modules/{baseAddress} | Get process information by its ID for a specific scaled-out instance in a web site.
[**webAppsGetInstanceProcessModuleSlot**](WebAppsApi.md#webAppsGetInstanceProcessModuleSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/processes/{processId}/modules/{baseAddress} | Get process information by its ID for a specific scaled-out instance in a web site.
[**webAppsGetInstanceProcessSlot**](WebAppsApi.md#webAppsGetInstanceProcessSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/processes/{processId} | Get process information by its ID for a specific scaled-out instance in a web site.
[**webAppsGetInstanceProcessThread**](WebAppsApi.md#webAppsGetInstanceProcessThread) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/processes/{processId}/threads/{threadId} | Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.
[**webAppsGetInstanceProcessThreadSlot**](WebAppsApi.md#webAppsGetInstanceProcessThreadSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/processes/{processId}/threads/{threadId} | Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.
[**webAppsGetMSDeployLog**](WebAppsApi.md#webAppsGetMSDeployLog) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/extensions/MSDeploy/log | Get the MSDeploy Log for the last MSDeploy operation.
[**webAppsGetMSDeployLogSlot**](WebAppsApi.md#webAppsGetMSDeployLogSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/extensions/MSDeploy/log | Get the MSDeploy Log for the last MSDeploy operation.
[**webAppsGetMSDeployStatus**](WebAppsApi.md#webAppsGetMSDeployStatus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/extensions/MSDeploy | Get the status of the last MSDeploy operation.
[**webAppsGetMSDeployStatusSlot**](WebAppsApi.md#webAppsGetMSDeployStatusSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/extensions/MSDeploy | Get the status of the last MSDeploy operation.
[**webAppsGetMigrateMySqlStatus**](WebAppsApi.md#webAppsGetMigrateMySqlStatus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/migratemysql/status | Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled
[**webAppsGetMigrateMySqlStatusSlot**](WebAppsApi.md#webAppsGetMigrateMySqlStatusSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/migratemysql/status | Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled
[**webAppsGetNetworkTraceOperation**](WebAppsApi.md#webAppsGetNetworkTraceOperation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/networkTrace/operationresults/{operationId} | Gets a named operation for a network trace capturing (or deployment slot, if specified).
[**webAppsGetNetworkTraceOperationSlot**](WebAppsApi.md#webAppsGetNetworkTraceOperationSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkTrace/operationresults/{operationId} | Gets a named operation for a network trace capturing (or deployment slot, if specified).
[**webAppsGetNetworkTraceOperationSlotV2**](WebAppsApi.md#webAppsGetNetworkTraceOperationSlotV2) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkTraces/current/operationresults/{operationId} | Gets a named operation for a network trace capturing (or deployment slot, if specified).
[**webAppsGetNetworkTraceOperationV2**](WebAppsApi.md#webAppsGetNetworkTraceOperationV2) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/networkTraces/current/operationresults/{operationId} | Gets a named operation for a network trace capturing (or deployment slot, if specified).
[**webAppsGetNetworkTraces**](WebAppsApi.md#webAppsGetNetworkTraces) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/networkTrace/{operationId} | Gets a named operation for a network trace capturing (or deployment slot, if specified).
[**webAppsGetNetworkTracesSlot**](WebAppsApi.md#webAppsGetNetworkTracesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkTrace/{operationId} | Gets a named operation for a network trace capturing (or deployment slot, if specified).
[**webAppsGetNetworkTracesSlotV2**](WebAppsApi.md#webAppsGetNetworkTracesSlotV2) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkTraces/{operationId} | Gets a named operation for a network trace capturing (or deployment slot, if specified).
[**webAppsGetNetworkTracesV2**](WebAppsApi.md#webAppsGetNetworkTracesV2) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/networkTraces/{operationId} | Gets a named operation for a network trace capturing (or deployment slot, if specified).
[**webAppsGetPremierAddOn**](WebAppsApi.md#webAppsGetPremierAddOn) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons/{premierAddOnName} | Gets a named add-on of an app.
[**webAppsGetPremierAddOnSlot**](WebAppsApi.md#webAppsGetPremierAddOnSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premierAddOnName} | Gets a named add-on of an app.
[**webAppsGetPrivateAccess**](WebAppsApi.md#webAppsGetPrivateAccess) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/privateAccess/virtualNetworks | Gets data around private site access enablement and authorized Virtual Networks that can access the site.
[**webAppsGetPrivateAccessSlot**](WebAppsApi.md#webAppsGetPrivateAccessSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/privateAccess/virtualNetworks | Gets data around private site access enablement and authorized Virtual Networks that can access the site.
[**webAppsGetProcess**](WebAppsApi.md#webAppsGetProcess) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/processes/{processId} | Get process information by its ID for a specific scaled-out instance in a web site.
[**webAppsGetProcessDump**](WebAppsApi.md#webAppsGetProcessDump) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/processes/{processId}/dump | Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.
[**webAppsGetProcessDumpSlot**](WebAppsApi.md#webAppsGetProcessDumpSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes/{processId}/dump | Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.
[**webAppsGetProcessModule**](WebAppsApi.md#webAppsGetProcessModule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/processes/{processId}/modules/{baseAddress} | Get process information by its ID for a specific scaled-out instance in a web site.
[**webAppsGetProcessModuleSlot**](WebAppsApi.md#webAppsGetProcessModuleSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes/{processId}/modules/{baseAddress} | Get process information by its ID for a specific scaled-out instance in a web site.
[**webAppsGetProcessSlot**](WebAppsApi.md#webAppsGetProcessSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes/{processId} | Get process information by its ID for a specific scaled-out instance in a web site.
[**webAppsGetProcessThread**](WebAppsApi.md#webAppsGetProcessThread) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/processes/{processId}/threads/{threadId} | Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.
[**webAppsGetProcessThreadSlot**](WebAppsApi.md#webAppsGetProcessThreadSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes/{processId}/threads/{threadId} | Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.
[**webAppsGetPublicCertificate**](WebAppsApi.md#webAppsGetPublicCertificate) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/publicCertificates/{publicCertificateName} | Get the named public certificate for an app (or deployment slot, if specified).
[**webAppsGetPublicCertificateSlot**](WebAppsApi.md#webAppsGetPublicCertificateSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/publicCertificates/{publicCertificateName} | Get the named public certificate for an app (or deployment slot, if specified).
[**webAppsGetRelayServiceConnection**](WebAppsApi.md#webAppsGetRelayServiceConnection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entityName} | Gets a hybrid connection configuration by its name.
[**webAppsGetRelayServiceConnectionSlot**](WebAppsApi.md#webAppsGetRelayServiceConnectionSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entityName} | Gets a hybrid connection configuration by its name.
[**webAppsGetSiteExtension**](WebAppsApi.md#webAppsGetSiteExtension) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/siteextensions/{siteExtensionId} | Get site extension information by its ID for a web site, or a deployment slot.
[**webAppsGetSiteExtensionSlot**](WebAppsApi.md#webAppsGetSiteExtensionSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/siteextensions/{siteExtensionId} | Get site extension information by its ID for a web site, or a deployment slot.
[**webAppsGetSitePhpErrorLogFlag**](WebAppsApi.md#webAppsGetSitePhpErrorLogFlag) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/phplogging | Gets web app&#39;s event logs.
[**webAppsGetSitePhpErrorLogFlagSlot**](WebAppsApi.md#webAppsGetSitePhpErrorLogFlagSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/phplogging | Gets web app&#39;s event logs.
[**webAppsGetSlot**](WebAppsApi.md#webAppsGetSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot} | Gets the details of a web, mobile, or API app.
[**webAppsGetSourceControl**](WebAppsApi.md#webAppsGetSourceControl) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web | Gets the source control configuration of an app.
[**webAppsGetSourceControlSlot**](WebAppsApi.md#webAppsGetSourceControlSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web | Gets the source control configuration of an app.
[**webAppsGetSwiftVirtualNetworkConnection**](WebAppsApi.md#webAppsGetSwiftVirtualNetworkConnection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/networkConfig/virtualNetwork | Gets a Swift Virtual Network connection.
[**webAppsGetSwiftVirtualNetworkConnectionSlot**](WebAppsApi.md#webAppsGetSwiftVirtualNetworkConnectionSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkConfig/virtualNetwork | Gets a Swift Virtual Network connection.
[**webAppsGetTriggeredWebJob**](WebAppsApi.md#webAppsGetTriggeredWebJob) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/triggeredwebjobs/{webJobName} | Gets a triggered web job by its ID for an app, or a deployment slot.
[**webAppsGetTriggeredWebJobHistory**](WebAppsApi.md#webAppsGetTriggeredWebJobHistory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/triggeredwebjobs/{webJobName}/history/{id} | Gets a triggered web job&#39;s history by its ID for an app, , or a deployment slot.
[**webAppsGetTriggeredWebJobHistorySlot**](WebAppsApi.md#webAppsGetTriggeredWebJobHistorySlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/triggeredwebjobs/{webJobName}/history/{id} | Gets a triggered web job&#39;s history by its ID for an app, , or a deployment slot.
[**webAppsGetTriggeredWebJobSlot**](WebAppsApi.md#webAppsGetTriggeredWebJobSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/triggeredwebjobs/{webJobName} | Gets a triggered web job by its ID for an app, or a deployment slot.
[**webAppsGetVnetConnection**](WebAppsApi.md#webAppsGetVnetConnection) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName} | Gets a virtual network the app (or deployment slot) is connected to by name.
[**webAppsGetVnetConnectionGateway**](WebAppsApi.md#webAppsGetVnetConnectionGateway) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Gets an app&#39;s Virtual Network gateway.
[**webAppsGetVnetConnectionGatewaySlot**](WebAppsApi.md#webAppsGetVnetConnectionGatewaySlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Gets an app&#39;s Virtual Network gateway.
[**webAppsGetVnetConnectionSlot**](WebAppsApi.md#webAppsGetVnetConnectionSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName} | Gets a virtual network the app (or deployment slot) is connected to by name.
[**webAppsGetWebJob**](WebAppsApi.md#webAppsGetWebJob) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/webjobs/{webJobName} | Get webjob information for an app, or a deployment slot.
[**webAppsGetWebJobSlot**](WebAppsApi.md#webAppsGetWebJobSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/webjobs/{webJobName} | Get webjob information for an app, or a deployment slot.
[**webAppsGetWebSiteContainerLogs**](WebAppsApi.md#webAppsGetWebSiteContainerLogs) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/containerlogs | Gets the last lines of docker logs for the given site
[**webAppsGetWebSiteContainerLogsSlot**](WebAppsApi.md#webAppsGetWebSiteContainerLogsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/containerlogs | Gets the last lines of docker logs for the given site
[**webAppsInstallSiteExtension**](WebAppsApi.md#webAppsInstallSiteExtension) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/siteextensions/{siteExtensionId} | Install site extension on a web site, or a deployment slot.
[**webAppsInstallSiteExtensionSlot**](WebAppsApi.md#webAppsInstallSiteExtensionSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/siteextensions/{siteExtensionId} | Install site extension on a web site, or a deployment slot.
[**webAppsIsCloneable**](WebAppsApi.md#webAppsIsCloneable) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/iscloneable | Shows whether an app can be cloned to another resource group or subscription.
[**webAppsIsCloneableSlot**](WebAppsApi.md#webAppsIsCloneableSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/iscloneable | Shows whether an app can be cloned to another resource group or subscription.
[**webAppsList**](WebAppsApi.md#webAppsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/sites | Get all apps for a subscription.
[**webAppsListApplicationSettings**](WebAppsApi.md#webAppsListApplicationSettings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/appsettings/list | Gets the application settings of an app.
[**webAppsListApplicationSettingsSlot**](WebAppsApi.md#webAppsListApplicationSettingsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/appsettings/list | Gets the application settings of an app.
[**webAppsListAzureStorageAccounts**](WebAppsApi.md#webAppsListAzureStorageAccounts) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/azurestorageaccounts/list | Gets the Azure storage account configurations of an app.
[**webAppsListAzureStorageAccountsSlot**](WebAppsApi.md#webAppsListAzureStorageAccountsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/azurestorageaccounts/list | Gets the Azure storage account configurations of an app.
[**webAppsListBackupStatusSecrets**](WebAppsApi.md#webAppsListBackupStatusSecrets) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups/{backupId}/list | Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.
[**webAppsListBackupStatusSecretsSlot**](WebAppsApi.md#webAppsListBackupStatusSecretsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backupId}/list | Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.
[**webAppsListBackups**](WebAppsApi.md#webAppsListBackups) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups | Gets existing backups of an app.
[**webAppsListBackupsSlot**](WebAppsApi.md#webAppsListBackupsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups | Gets existing backups of an app.
[**webAppsListByResourceGroup**](WebAppsApi.md#webAppsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites | Gets all web, mobile, and API apps in the specified resource group.
[**webAppsListConfigurationSnapshotInfo**](WebAppsApi.md#webAppsListConfigurationSnapshotInfo) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/web/snapshots | Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.
[**webAppsListConfigurationSnapshotInfoSlot**](WebAppsApi.md#webAppsListConfigurationSnapshotInfoSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web/snapshots | Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.
[**webAppsListConfigurations**](WebAppsApi.md#webAppsListConfigurations) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config | List the configurations of an app
[**webAppsListConfigurationsSlot**](WebAppsApi.md#webAppsListConfigurationsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config | List the configurations of an app
[**webAppsListConnectionStrings**](WebAppsApi.md#webAppsListConnectionStrings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/connectionstrings/list | Gets the connection strings of an app.
[**webAppsListConnectionStringsSlot**](WebAppsApi.md#webAppsListConnectionStringsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/connectionstrings/list | Gets the connection strings of an app.
[**webAppsListContinuousWebJobs**](WebAppsApi.md#webAppsListContinuousWebJobs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/continuouswebjobs | List continuous web jobs for an app, or a deployment slot.
[**webAppsListContinuousWebJobsSlot**](WebAppsApi.md#webAppsListContinuousWebJobsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/continuouswebjobs | List continuous web jobs for an app, or a deployment slot.
[**webAppsListDeploymentLog**](WebAppsApi.md#webAppsListDeploymentLog) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/deployments/{id}/log | List deployment log for specific deployment for an app, or a deployment slot.
[**webAppsListDeploymentLogSlot**](WebAppsApi.md#webAppsListDeploymentLogSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments/{id}/log | List deployment log for specific deployment for an app, or a deployment slot.
[**webAppsListDeployments**](WebAppsApi.md#webAppsListDeployments) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/deployments | List deployments for an app, or a deployment slot.
[**webAppsListDeploymentsSlot**](WebAppsApi.md#webAppsListDeploymentsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/deployments | List deployments for an app, or a deployment slot.
[**webAppsListDomainOwnershipIdentifiers**](WebAppsApi.md#webAppsListDomainOwnershipIdentifiers) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/domainOwnershipIdentifiers | Lists ownership identifiers for domain associated with web app.
[**webAppsListDomainOwnershipIdentifiersSlot**](WebAppsApi.md#webAppsListDomainOwnershipIdentifiersSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/domainOwnershipIdentifiers | Lists ownership identifiers for domain associated with web app.
[**webAppsListFunctionKeys**](WebAppsApi.md#webAppsListFunctionKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/functions/{functionName}/listkeys | Get function keys for a function in a web site, or a deployment slot.
[**webAppsListFunctionKeysSlot**](WebAppsApi.md#webAppsListFunctionKeysSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/{functionName}/listkeys | Get function keys for a function in a web site, or a deployment slot.
[**webAppsListFunctionSecrets**](WebAppsApi.md#webAppsListFunctionSecrets) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/functions/{functionName}/listsecrets | Get function secrets for a function in a web site, or a deployment slot.
[**webAppsListFunctionSecretsSlot**](WebAppsApi.md#webAppsListFunctionSecretsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions/{functionName}/listsecrets | Get function secrets for a function in a web site, or a deployment slot.
[**webAppsListFunctions**](WebAppsApi.md#webAppsListFunctions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/functions | List the functions for a web site, or a deployment slot.
[**webAppsListHostKeys**](WebAppsApi.md#webAppsListHostKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/host/default/listkeys | Get host secrets for a function app.
[**webAppsListHostKeysSlot**](WebAppsApi.md#webAppsListHostKeysSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/host/default/listkeys | Get host secrets for a function app.
[**webAppsListHostNameBindings**](WebAppsApi.md#webAppsListHostNameBindings) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hostNameBindings | Get hostname bindings for an app or a deployment slot.
[**webAppsListHostNameBindingsSlot**](WebAppsApi.md#webAppsListHostNameBindingsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hostNameBindings | Get hostname bindings for an app or a deployment slot.
[**webAppsListHybridConnectionKeys**](WebAppsApi.md#webAppsListHybridConnectionKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName}/listKeys | Gets the send key name and value for a Hybrid Connection.
[**webAppsListHybridConnectionKeysSlot**](WebAppsApi.md#webAppsListHybridConnectionKeysSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName}/listKeys | Gets the send key name and value for a Hybrid Connection.
[**webAppsListHybridConnections**](WebAppsApi.md#webAppsListHybridConnections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridConnectionRelays | Retrieves all Service Bus Hybrid Connections used by this Web App.
[**webAppsListHybridConnectionsSlot**](WebAppsApi.md#webAppsListHybridConnectionsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridConnectionRelays | Retrieves all Service Bus Hybrid Connections used by this Web App.
[**webAppsListInstanceFunctionsSlot**](WebAppsApi.md#webAppsListInstanceFunctionsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/functions | List the functions for a web site, or a deployment slot.
[**webAppsListInstanceIdentifiers**](WebAppsApi.md#webAppsListInstanceIdentifiers) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances | Gets all scale-out instances of an app.
[**webAppsListInstanceIdentifiersSlot**](WebAppsApi.md#webAppsListInstanceIdentifiersSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances | Gets all scale-out instances of an app.
[**webAppsListInstanceProcessModules**](WebAppsApi.md#webAppsListInstanceProcessModules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/processes/{processId}/modules | List module information for a process by its ID for a specific scaled-out instance in a web site.
[**webAppsListInstanceProcessModulesSlot**](WebAppsApi.md#webAppsListInstanceProcessModulesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/processes/{processId}/modules | List module information for a process by its ID for a specific scaled-out instance in a web site.
[**webAppsListInstanceProcessThreads**](WebAppsApi.md#webAppsListInstanceProcessThreads) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/processes/{processId}/threads | List the threads in a process by its ID for a specific scaled-out instance in a web site.
[**webAppsListInstanceProcessThreadsSlot**](WebAppsApi.md#webAppsListInstanceProcessThreadsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/processes/{processId}/threads | List the threads in a process by its ID for a specific scaled-out instance in a web site.
[**webAppsListInstanceProcesses**](WebAppsApi.md#webAppsListInstanceProcesses) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/instances/{instanceId}/processes | Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.
[**webAppsListInstanceProcessesSlot**](WebAppsApi.md#webAppsListInstanceProcessesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/instances/{instanceId}/processes | Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.
[**webAppsListMetadata**](WebAppsApi.md#webAppsListMetadata) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/metadata/list | Gets the metadata of an app.
[**webAppsListMetadataSlot**](WebAppsApi.md#webAppsListMetadataSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/metadata/list | Gets the metadata of an app.
[**webAppsListMetricDefinitions**](WebAppsApi.md#webAppsListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/metricdefinitions | Gets all metric definitions of an app (or deployment slot, if specified).
[**webAppsListMetricDefinitionsSlot**](WebAppsApi.md#webAppsListMetricDefinitionsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/metricdefinitions | Gets all metric definitions of an app (or deployment slot, if specified).
[**webAppsListMetrics**](WebAppsApi.md#webAppsListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/metrics | Gets performance metrics of an app (or deployment slot, if specified).
[**webAppsListMetricsSlot**](WebAppsApi.md#webAppsListMetricsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/metrics | Gets performance metrics of an app (or deployment slot, if specified).
[**webAppsListNetworkFeatures**](WebAppsApi.md#webAppsListNetworkFeatures) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/networkFeatures/{view} | Gets all network features used by the app (or deployment slot, if specified).
[**webAppsListNetworkFeaturesSlot**](WebAppsApi.md#webAppsListNetworkFeaturesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkFeatures/{view} | Gets all network features used by the app (or deployment slot, if specified).
[**webAppsListPerfMonCounters**](WebAppsApi.md#webAppsListPerfMonCounters) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/perfcounters | Gets perfmon counters for web app.
[**webAppsListPerfMonCountersSlot**](WebAppsApi.md#webAppsListPerfMonCountersSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/perfcounters | Gets perfmon counters for web app.
[**webAppsListPremierAddOns**](WebAppsApi.md#webAppsListPremierAddOns) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons | Gets the premier add-ons of an app.
[**webAppsListPremierAddOnsSlot**](WebAppsApi.md#webAppsListPremierAddOnsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons | Gets the premier add-ons of an app.
[**webAppsListProcessModules**](WebAppsApi.md#webAppsListProcessModules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/processes/{processId}/modules | List module information for a process by its ID for a specific scaled-out instance in a web site.
[**webAppsListProcessModulesSlot**](WebAppsApi.md#webAppsListProcessModulesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes/{processId}/modules | List module information for a process by its ID for a specific scaled-out instance in a web site.
[**webAppsListProcessThreads**](WebAppsApi.md#webAppsListProcessThreads) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/processes/{processId}/threads | List the threads in a process by its ID for a specific scaled-out instance in a web site.
[**webAppsListProcessThreadsSlot**](WebAppsApi.md#webAppsListProcessThreadsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes/{processId}/threads | List the threads in a process by its ID for a specific scaled-out instance in a web site.
[**webAppsListProcesses**](WebAppsApi.md#webAppsListProcesses) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/processes | Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.
[**webAppsListProcessesSlot**](WebAppsApi.md#webAppsListProcessesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/processes | Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.
[**webAppsListPublicCertificates**](WebAppsApi.md#webAppsListPublicCertificates) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/publicCertificates | Get public certificates for an app or a deployment slot.
[**webAppsListPublicCertificatesSlot**](WebAppsApi.md#webAppsListPublicCertificatesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/publicCertificates | Get public certificates for an app or a deployment slot.
[**webAppsListPublishingCredentials**](WebAppsApi.md#webAppsListPublishingCredentials) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/publishingcredentials/list | Gets the Git/FTP publishing credentials of an app.
[**webAppsListPublishingCredentialsSlot**](WebAppsApi.md#webAppsListPublishingCredentialsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/publishingcredentials/list | Gets the Git/FTP publishing credentials of an app.
[**webAppsListPublishingProfileXmlWithSecrets**](WebAppsApi.md#webAppsListPublishingProfileXmlWithSecrets) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/publishxml | Gets the publishing profile for an app (or deployment slot, if specified).
[**webAppsListPublishingProfileXmlWithSecretsSlot**](WebAppsApi.md#webAppsListPublishingProfileXmlWithSecretsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/publishxml | Gets the publishing profile for an app (or deployment slot, if specified).
[**webAppsListRelayServiceConnections**](WebAppsApi.md#webAppsListRelayServiceConnections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection | Gets hybrid connections configured for an app (or deployment slot, if specified).
[**webAppsListRelayServiceConnectionsSlot**](WebAppsApi.md#webAppsListRelayServiceConnectionsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection | Gets hybrid connections configured for an app (or deployment slot, if specified).
[**webAppsListSiteExtensions**](WebAppsApi.md#webAppsListSiteExtensions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/siteextensions | Get list of siteextensions for a web site, or a deployment slot.
[**webAppsListSiteExtensionsSlot**](WebAppsApi.md#webAppsListSiteExtensionsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/siteextensions | Get list of siteextensions for a web site, or a deployment slot.
[**webAppsListSitePushSettings**](WebAppsApi.md#webAppsListSitePushSettings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/pushsettings/list | Gets the Push settings associated with web app.
[**webAppsListSitePushSettingsSlot**](WebAppsApi.md#webAppsListSitePushSettingsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/pushsettings/list | Gets the Push settings associated with web app.
[**webAppsListSlotConfigurationNames**](WebAppsApi.md#webAppsListSlotConfigurationNames) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/slotConfigNames | Gets the names of app settings and connection strings that stick to the slot (not swapped).
[**webAppsListSlotDifferencesFromProduction**](WebAppsApi.md#webAppsListSlotDifferencesFromProduction) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slotsdiffs | Get the difference in configuration settings between two web app slots.
[**webAppsListSlotDifferencesSlot**](WebAppsApi.md#webAppsListSlotDifferencesSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/slotsdiffs | Get the difference in configuration settings between two web app slots.
[**webAppsListSlots**](WebAppsApi.md#webAppsListSlots) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots | Gets an app&#39;s deployment slots.
[**webAppsListSnapshots**](WebAppsApi.md#webAppsListSnapshots) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/snapshots | Returns all Snapshots to the user.
[**webAppsListSnapshotsFromDRSecondary**](WebAppsApi.md#webAppsListSnapshotsFromDRSecondary) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/snapshotsdr | Returns all Snapshots to the user from DRSecondary endpoint.
[**webAppsListSnapshotsFromDRSecondarySlot**](WebAppsApi.md#webAppsListSnapshotsFromDRSecondarySlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/snapshotsdr | Returns all Snapshots to the user from DRSecondary endpoint.
[**webAppsListSnapshotsSlot**](WebAppsApi.md#webAppsListSnapshotsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/snapshots | Returns all Snapshots to the user.
[**webAppsListSyncFunctionTriggers**](WebAppsApi.md#webAppsListSyncFunctionTriggers) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/listsyncfunctiontriggerstatus | This is to allow calling via powershell and ARM template.
[**webAppsListSyncFunctionTriggersSlot**](WebAppsApi.md#webAppsListSyncFunctionTriggersSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/listsyncfunctiontriggerstatus | This is to allow calling via powershell and ARM template.
[**webAppsListSyncStatus**](WebAppsApi.md#webAppsListSyncStatus) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/host/default/listsyncstatus | This is to allow calling via powershell and ARM template.
[**webAppsListSyncStatusSlot**](WebAppsApi.md#webAppsListSyncStatusSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/host/default/listsyncstatus | This is to allow calling via powershell and ARM template.
[**webAppsListTriggeredWebJobHistory**](WebAppsApi.md#webAppsListTriggeredWebJobHistory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/triggeredwebjobs/{webJobName}/history | List a triggered web job&#39;s history for an app, or a deployment slot.
[**webAppsListTriggeredWebJobHistorySlot**](WebAppsApi.md#webAppsListTriggeredWebJobHistorySlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/triggeredwebjobs/{webJobName}/history | List a triggered web job&#39;s history for an app, or a deployment slot.
[**webAppsListTriggeredWebJobs**](WebAppsApi.md#webAppsListTriggeredWebJobs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/triggeredwebjobs | List triggered web jobs for an app, or a deployment slot.
[**webAppsListTriggeredWebJobsSlot**](WebAppsApi.md#webAppsListTriggeredWebJobsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/triggeredwebjobs | List triggered web jobs for an app, or a deployment slot.
[**webAppsListUsages**](WebAppsApi.md#webAppsListUsages) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/usages | Gets the quota usage information of an app (or deployment slot, if specified).
[**webAppsListUsagesSlot**](WebAppsApi.md#webAppsListUsagesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/usages | Gets the quota usage information of an app (or deployment slot, if specified).
[**webAppsListVnetConnections**](WebAppsApi.md#webAppsListVnetConnections) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections | Gets the virtual networks the app (or deployment slot) is connected to.
[**webAppsListVnetConnectionsSlot**](WebAppsApi.md#webAppsListVnetConnectionsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections | Gets the virtual networks the app (or deployment slot) is connected to.
[**webAppsListWebJobs**](WebAppsApi.md#webAppsListWebJobs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/webjobs | List webjobs for an app, or a deployment slot.
[**webAppsListWebJobsSlot**](WebAppsApi.md#webAppsListWebJobsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/webjobs | List webjobs for an app, or a deployment slot.
[**webAppsMigrateMySql**](WebAppsApi.md#webAppsMigrateMySql) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/migratemysql | Migrates a local (in-app) MySql database to a remote MySql database.
[**webAppsMigrateStorage**](WebAppsApi.md#webAppsMigrateStorage) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/migrate | Restores a web app.
[**webAppsPutPrivateAccessVnet**](WebAppsApi.md#webAppsPutPrivateAccessVnet) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/privateAccess/virtualNetworks | Sets data around private site access enablement and authorized Virtual Networks that can access the site.
[**webAppsPutPrivateAccessVnetSlot**](WebAppsApi.md#webAppsPutPrivateAccessVnetSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/privateAccess/virtualNetworks | Sets data around private site access enablement and authorized Virtual Networks that can access the site.
[**webAppsRecoverSiteConfigurationSnapshot**](WebAppsApi.md#webAppsRecoverSiteConfigurationSnapshot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/web/snapshots/{snapshotId}/recover | Reverts the configuration of an app to a previous snapshot.
[**webAppsRecoverSiteConfigurationSnapshotSlot**](WebAppsApi.md#webAppsRecoverSiteConfigurationSnapshotSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web/snapshots/{snapshotId}/recover | Reverts the configuration of an app to a previous snapshot.
[**webAppsResetProductionSlotConfig**](WebAppsApi.md#webAppsResetProductionSlotConfig) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/resetSlotConfig | Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.
[**webAppsResetSlotConfigurationSlot**](WebAppsApi.md#webAppsResetSlotConfigurationSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/resetSlotConfig | Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.
[**webAppsRestart**](WebAppsApi.md#webAppsRestart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/restart | Restarts an app (or deployment slot, if specified).
[**webAppsRestartSlot**](WebAppsApi.md#webAppsRestartSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/restart | Restarts an app (or deployment slot, if specified).
[**webAppsRestore**](WebAppsApi.md#webAppsRestore) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/backups/{backupId}/restore | Restores a specific backup to another app (or deployment slot, if specified).
[**webAppsRestoreFromBackupBlob**](WebAppsApi.md#webAppsRestoreFromBackupBlob) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/restoreFromBackupBlob | Restores an app from a backup blob in Azure Storage.
[**webAppsRestoreFromBackupBlobSlot**](WebAppsApi.md#webAppsRestoreFromBackupBlobSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/restoreFromBackupBlob | Restores an app from a backup blob in Azure Storage.
[**webAppsRestoreFromDeletedApp**](WebAppsApi.md#webAppsRestoreFromDeletedApp) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/restoreFromDeletedApp | Restores a deleted web app to this web app.
[**webAppsRestoreFromDeletedAppSlot**](WebAppsApi.md#webAppsRestoreFromDeletedAppSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/restoreFromDeletedApp | Restores a deleted web app to this web app.
[**webAppsRestoreSlot**](WebAppsApi.md#webAppsRestoreSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/backups/{backupId}/restore | Restores a specific backup to another app (or deployment slot, if specified).
[**webAppsRestoreSnapshot**](WebAppsApi.md#webAppsRestoreSnapshot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/restoreSnapshot | Restores a web app from a snapshot.
[**webAppsRestoreSnapshotSlot**](WebAppsApi.md#webAppsRestoreSnapshotSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/restoreSnapshot | Restores a web app from a snapshot.
[**webAppsRunTriggeredWebJob**](WebAppsApi.md#webAppsRunTriggeredWebJob) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/triggeredwebjobs/{webJobName}/run | Run a triggered web job for an app, or a deployment slot.
[**webAppsRunTriggeredWebJobSlot**](WebAppsApi.md#webAppsRunTriggeredWebJobSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/triggeredwebjobs/{webJobName}/run | Run a triggered web job for an app, or a deployment slot.
[**webAppsStart**](WebAppsApi.md#webAppsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/start | Starts an app (or deployment slot, if specified).
[**webAppsStartContinuousWebJob**](WebAppsApi.md#webAppsStartContinuousWebJob) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/continuouswebjobs/{webJobName}/start | Start a continuous web job for an app, or a deployment slot.
[**webAppsStartContinuousWebJobSlot**](WebAppsApi.md#webAppsStartContinuousWebJobSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/continuouswebjobs/{webJobName}/start | Start a continuous web job for an app, or a deployment slot.
[**webAppsStartNetworkTrace**](WebAppsApi.md#webAppsStartNetworkTrace) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/startNetworkTrace | Start capturing network packets for the site.
[**webAppsStartNetworkTraceSlot**](WebAppsApi.md#webAppsStartNetworkTraceSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/startNetworkTrace | Start capturing network packets for the site.
[**webAppsStartSlot**](WebAppsApi.md#webAppsStartSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/start | Starts an app (or deployment slot, if specified).
[**webAppsStartWebSiteNetworkTrace**](WebAppsApi.md#webAppsStartWebSiteNetworkTrace) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/networkTrace/start | Start capturing network packets for the site (To be deprecated).
[**webAppsStartWebSiteNetworkTraceOperation**](WebAppsApi.md#webAppsStartWebSiteNetworkTraceOperation) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/networkTrace/startOperation | Start capturing network packets for the site.
[**webAppsStartWebSiteNetworkTraceOperationSlot**](WebAppsApi.md#webAppsStartWebSiteNetworkTraceOperationSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkTrace/startOperation | Start capturing network packets for the site.
[**webAppsStartWebSiteNetworkTraceSlot**](WebAppsApi.md#webAppsStartWebSiteNetworkTraceSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkTrace/start | Start capturing network packets for the site (To be deprecated).
[**webAppsStop**](WebAppsApi.md#webAppsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/stop | Stops an app (or deployment slot, if specified).
[**webAppsStopContinuousWebJob**](WebAppsApi.md#webAppsStopContinuousWebJob) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/continuouswebjobs/{webJobName}/stop | Stop a continuous web job for an app, or a deployment slot.
[**webAppsStopContinuousWebJobSlot**](WebAppsApi.md#webAppsStopContinuousWebJobSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/continuouswebjobs/{webJobName}/stop | Stop a continuous web job for an app, or a deployment slot.
[**webAppsStopNetworkTrace**](WebAppsApi.md#webAppsStopNetworkTrace) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/stopNetworkTrace | Stop ongoing capturing network packets for the site.
[**webAppsStopNetworkTraceSlot**](WebAppsApi.md#webAppsStopNetworkTraceSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/stopNetworkTrace | Stop ongoing capturing network packets for the site.
[**webAppsStopSlot**](WebAppsApi.md#webAppsStopSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/stop | Stops an app (or deployment slot, if specified).
[**webAppsStopWebSiteNetworkTrace**](WebAppsApi.md#webAppsStopWebSiteNetworkTrace) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/networkTrace/stop | Stop ongoing capturing network packets for the site.
[**webAppsStopWebSiteNetworkTraceSlot**](WebAppsApi.md#webAppsStopWebSiteNetworkTraceSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkTrace/stop | Stop ongoing capturing network packets for the site.
[**webAppsSwapSlotSlot**](WebAppsApi.md#webAppsSwapSlotSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/slotsswap | Swaps two deployment slots of an app.
[**webAppsSwapSlotWithProduction**](WebAppsApi.md#webAppsSwapSlotWithProduction) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slotsswap | Swaps two deployment slots of an app.
[**webAppsSyncFunctionTriggers**](WebAppsApi.md#webAppsSyncFunctionTriggers) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/syncfunctiontriggers | Syncs function trigger metadata to the management database
[**webAppsSyncFunctionTriggersSlot**](WebAppsApi.md#webAppsSyncFunctionTriggersSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/syncfunctiontriggers | Syncs function trigger metadata to the management database
[**webAppsSyncFunctions**](WebAppsApi.md#webAppsSyncFunctions) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/host/default/sync | Syncs function trigger metadata to the management database
[**webAppsSyncFunctionsSlot**](WebAppsApi.md#webAppsSyncFunctionsSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/host/default/sync | Syncs function trigger metadata to the management database
[**webAppsSyncRepository**](WebAppsApi.md#webAppsSyncRepository) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sync | Sync web app repository.
[**webAppsSyncRepositorySlot**](WebAppsApi.md#webAppsSyncRepositorySlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sync | Sync web app repository.
[**webAppsUpdate**](WebAppsApi.md#webAppsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name} | Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.
[**webAppsUpdateApplicationSettings**](WebAppsApi.md#webAppsUpdateApplicationSettings) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/appsettings | Replaces the application settings of an app.
[**webAppsUpdateApplicationSettingsSlot**](WebAppsApi.md#webAppsUpdateApplicationSettingsSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/appsettings | Replaces the application settings of an app.
[**webAppsUpdateAuthSettings**](WebAppsApi.md#webAppsUpdateAuthSettings) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/authsettings | Updates the Authentication / Authorization settings associated with web app.
[**webAppsUpdateAuthSettingsSlot**](WebAppsApi.md#webAppsUpdateAuthSettingsSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/authsettings | Updates the Authentication / Authorization settings associated with web app.
[**webAppsUpdateAzureStorageAccounts**](WebAppsApi.md#webAppsUpdateAzureStorageAccounts) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/azurestorageaccounts | Updates the Azure storage account configurations of an app.
[**webAppsUpdateAzureStorageAccountsSlot**](WebAppsApi.md#webAppsUpdateAzureStorageAccountsSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/azurestorageaccounts | Updates the Azure storage account configurations of an app.
[**webAppsUpdateBackupConfiguration**](WebAppsApi.md#webAppsUpdateBackupConfiguration) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/backup | Updates the backup configuration of an app.
[**webAppsUpdateBackupConfigurationSlot**](WebAppsApi.md#webAppsUpdateBackupConfigurationSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/backup | Updates the backup configuration of an app.
[**webAppsUpdateConfiguration**](WebAppsApi.md#webAppsUpdateConfiguration) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/web | Updates the configuration of an app.
[**webAppsUpdateConfigurationSlot**](WebAppsApi.md#webAppsUpdateConfigurationSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/web | Updates the configuration of an app.
[**webAppsUpdateConnectionStrings**](WebAppsApi.md#webAppsUpdateConnectionStrings) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/connectionstrings | Replaces the connection strings of an app.
[**webAppsUpdateConnectionStringsSlot**](WebAppsApi.md#webAppsUpdateConnectionStringsSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/connectionstrings | Replaces the connection strings of an app.
[**webAppsUpdateDiagnosticLogsConfig**](WebAppsApi.md#webAppsUpdateDiagnosticLogsConfig) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/logs | Updates the logging configuration of an app.
[**webAppsUpdateDiagnosticLogsConfigSlot**](WebAppsApi.md#webAppsUpdateDiagnosticLogsConfigSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/logs | Updates the logging configuration of an app.
[**webAppsUpdateDomainOwnershipIdentifier**](WebAppsApi.md#webAppsUpdateDomainOwnershipIdentifier) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/domainOwnershipIdentifiers/{domainOwnershipIdentifierName} | Creates a domain ownership identifier for web app, or updates an existing ownership identifier.
[**webAppsUpdateDomainOwnershipIdentifierSlot**](WebAppsApi.md#webAppsUpdateDomainOwnershipIdentifierSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/domainOwnershipIdentifiers/{domainOwnershipIdentifierName} | Creates a domain ownership identifier for web app, or updates an existing ownership identifier.
[**webAppsUpdateHybridConnection**](WebAppsApi.md#webAppsUpdateHybridConnection) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName} | Creates a new Hybrid Connection using a Service Bus relay.
[**webAppsUpdateHybridConnectionSlot**](WebAppsApi.md#webAppsUpdateHybridConnectionSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridConnectionNamespaces/{namespaceName}/relays/{relayName} | Creates a new Hybrid Connection using a Service Bus relay.
[**webAppsUpdateMetadata**](WebAppsApi.md#webAppsUpdateMetadata) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/metadata | Replaces the metadata of an app.
[**webAppsUpdateMetadataSlot**](WebAppsApi.md#webAppsUpdateMetadataSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/metadata | Replaces the metadata of an app.
[**webAppsUpdatePremierAddOn**](WebAppsApi.md#webAppsUpdatePremierAddOn) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/premieraddons/{premierAddOnName} | Updates a named add-on of an app.
[**webAppsUpdatePremierAddOnSlot**](WebAppsApi.md#webAppsUpdatePremierAddOnSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/premieraddons/{premierAddOnName} | Updates a named add-on of an app.
[**webAppsUpdateRelayServiceConnection**](WebAppsApi.md#webAppsUpdateRelayServiceConnection) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/hybridconnection/{entityName} | Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).
[**webAppsUpdateRelayServiceConnectionSlot**](WebAppsApi.md#webAppsUpdateRelayServiceConnectionSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/hybridconnection/{entityName} | Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).
[**webAppsUpdateSitePushSettings**](WebAppsApi.md#webAppsUpdateSitePushSettings) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/pushsettings | Updates the Push settings associated with web app.
[**webAppsUpdateSitePushSettingsSlot**](WebAppsApi.md#webAppsUpdateSitePushSettingsSlot) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/config/pushsettings | Updates the Push settings associated with web app.
[**webAppsUpdateSlot**](WebAppsApi.md#webAppsUpdateSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot} | Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.
[**webAppsUpdateSlotConfigurationNames**](WebAppsApi.md#webAppsUpdateSlotConfigurationNames) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/config/slotConfigNames | Updates the names of application settings and connection string that remain with the slot during swap operation.
[**webAppsUpdateSourceControl**](WebAppsApi.md#webAppsUpdateSourceControl) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/sourcecontrols/web | Updates the source control configuration of an app.
[**webAppsUpdateSourceControlSlot**](WebAppsApi.md#webAppsUpdateSourceControlSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/sourcecontrols/web | Updates the source control configuration of an app.
[**webAppsUpdateSwiftVirtualNetworkConnection**](WebAppsApi.md#webAppsUpdateSwiftVirtualNetworkConnection) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/networkConfig/virtualNetwork | Integrates this Web App with a Virtual Network. This requires that 1) \&quot;swiftSupported\&quot; is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not  in use by another App Service Plan other than the one this App is in.
[**webAppsUpdateSwiftVirtualNetworkConnectionSlot**](WebAppsApi.md#webAppsUpdateSwiftVirtualNetworkConnectionSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/networkConfig/virtualNetwork | Integrates this Web App with a Virtual Network. This requires that 1) \&quot;swiftSupported\&quot; is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not  in use by another App Service Plan other than the one this App is in.
[**webAppsUpdateVnetConnection**](WebAppsApi.md#webAppsUpdateVnetConnection) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName} | Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).
[**webAppsUpdateVnetConnectionGateway**](WebAppsApi.md#webAppsUpdateVnetConnectionGateway) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).
[**webAppsUpdateVnetConnectionGatewaySlot**](WebAppsApi.md#webAppsUpdateVnetConnectionGatewaySlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName}/gateways/{gatewayName} | Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).
[**webAppsUpdateVnetConnectionSlot**](WebAppsApi.md#webAppsUpdateVnetConnectionSlot) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{name}/slots/{slot}/virtualNetworkConnections/{vnetName} | Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).



## webAppsAddPremierAddOn

> PremierAddOn webAppsAddPremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion, premierAddOn)

Updates a named add-on of an app.

Updates a named add-on of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let premierAddOnName = "premierAddOnName_example"; // String | Add-on name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let premierAddOn = new WebAppsApiClient.PremierAddOn(); // PremierAddOn | A JSON representation of the edited premier add-on.
apiInstance.webAppsAddPremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion, premierAddOn, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **premierAddOnName** | **String**| Add-on name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **premierAddOn** | [**PremierAddOn**](PremierAddOn.md)| A JSON representation of the edited premier add-on. | 

### Return type

[**PremierAddOn**](PremierAddOn.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsAddPremierAddOnSlot

> PremierAddOn webAppsAddPremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion, premierAddOn)

Updates a named add-on of an app.

Updates a named add-on of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let premierAddOnName = "premierAddOnName_example"; // String | Add-on name.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will update the named add-on for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let premierAddOn = new WebAppsApiClient.PremierAddOn(); // PremierAddOn | A JSON representation of the edited premier add-on.
apiInstance.webAppsAddPremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion, premierAddOn, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **premierAddOnName** | **String**| Add-on name. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will update the named add-on for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **premierAddOn** | [**PremierAddOn**](PremierAddOn.md)| A JSON representation of the edited premier add-on. | 

### Return type

[**PremierAddOn**](PremierAddOn.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsAnalyzeCustomHostname

> CustomHostnameAnalysisResult webAppsAnalyzeCustomHostname(resourceGroupName, name, subscriptionId, apiVersion, opts)

Analyze a custom hostname.

Analyze a custom hostname.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'hostName': "hostName_example" // String | Custom hostname.
};
apiInstance.webAppsAnalyzeCustomHostname(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **hostName** | **String**| Custom hostname. | [optional] 

### Return type

[**CustomHostnameAnalysisResult**](CustomHostnameAnalysisResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsAnalyzeCustomHostnameSlot

> CustomHostnameAnalysisResult webAppsAnalyzeCustomHostnameSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts)

Analyze a custom hostname.

Analyze a custom hostname.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'hostName': "hostName_example" // String | Custom hostname.
};
apiInstance.webAppsAnalyzeCustomHostnameSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **hostName** | **String**| Custom hostname. | [optional] 

### Return type

[**CustomHostnameAnalysisResult**](CustomHostnameAnalysisResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsApplySlotConfigToProduction

> webAppsApplySlotConfigToProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity)

Applies the configuration settings from the target slot onto the current slot.

Applies the configuration settings from the target slot onto the current slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let slotSwapEntity = new WebAppsApiClient.CsmSlotEntity(); // CsmSlotEntity | JSON object that contains the target slot name. See example.
apiInstance.webAppsApplySlotConfigToProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| JSON object that contains the target slot name. See example. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## webAppsApplySlotConfigurationSlot

> webAppsApplySlotConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity)

Applies the configuration settings from the target slot onto the current slot.

Applies the configuration settings from the target slot onto the current slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the source slot. If a slot is not specified, the production slot is used as the source slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let slotSwapEntity = new WebAppsApiClient.CsmSlotEntity(); // CsmSlotEntity | JSON object that contains the target slot name. See example.
apiInstance.webAppsApplySlotConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the source slot. If a slot is not specified, the production slot is used as the source slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| JSON object that contains the target slot name. See example. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## webAppsBackup

> BackupItem webAppsBackup(resourceGroupName, name, subscriptionId, apiVersion, request)

Creates a backup of an app.

Creates a backup of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebAppsApiClient.BackupRequest(); // BackupRequest | Backup configuration. You can use the JSON response from the POST action as input here.
apiInstance.webAppsBackup(resourceGroupName, name, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **request** | [**BackupRequest**](BackupRequest.md)| Backup configuration. You can use the JSON response from the POST action as input here. | 

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsBackupSlot

> BackupItem webAppsBackupSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request)

Creates a backup of an app.

Creates a backup of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will create a backup for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebAppsApiClient.BackupRequest(); // BackupRequest | Backup configuration. You can use the JSON response from the POST action as input here.
apiInstance.webAppsBackupSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will create a backup for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **request** | [**BackupRequest**](BackupRequest.md)| Backup configuration. You can use the JSON response from the POST action as input here. | 

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateDeployment

> Deployment webAppsCreateDeployment(resourceGroupName, name, id, subscriptionId, apiVersion, deployment)

Create a deployment for an app, or a deployment slot.

Create a deployment for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let id = "id_example"; // String | ID of an existing deployment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let deployment = new WebAppsApiClient.Deployment(); // Deployment | Deployment details.
apiInstance.webAppsCreateDeployment(resourceGroupName, name, id, subscriptionId, apiVersion, deployment, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **id** | **String**| ID of an existing deployment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **deployment** | [**Deployment**](Deployment.md)| Deployment details. | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateDeploymentSlot

> Deployment webAppsCreateDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion, deployment)

Create a deployment for an app, or a deployment slot.

Create a deployment for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let id = "id_example"; // String | ID of an existing deployment.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API creates a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let deployment = new WebAppsApiClient.Deployment(); // Deployment | Deployment details.
apiInstance.webAppsCreateDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion, deployment, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **id** | **String**| ID of an existing deployment. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API creates a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **deployment** | [**Deployment**](Deployment.md)| Deployment details. | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateFunction

> FunctionEnvelope webAppsCreateFunction(resourceGroupName, name, functionName, subscriptionId, apiVersion, functionEnvelope)

Create function for web site, or a deployment slot.

Create function for web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let functionName = "functionName_example"; // String | Function name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let functionEnvelope = new WebAppsApiClient.FunctionEnvelope(); // FunctionEnvelope | Function details.
apiInstance.webAppsCreateFunction(resourceGroupName, name, functionName, subscriptionId, apiVersion, functionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **functionName** | **String**| Function name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **functionEnvelope** | [**FunctionEnvelope**](FunctionEnvelope.md)| Function details. | 

### Return type

[**FunctionEnvelope**](FunctionEnvelope.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateInstanceFunctionSlot

> FunctionEnvelope webAppsCreateInstanceFunctionSlot(resourceGroupName, name, functionName, slot, subscriptionId, apiVersion, functionEnvelope)

Create function for web site, or a deployment slot.

Create function for web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let functionName = "functionName_example"; // String | Function name.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let functionEnvelope = new WebAppsApiClient.FunctionEnvelope(); // FunctionEnvelope | Function details.
apiInstance.webAppsCreateInstanceFunctionSlot(resourceGroupName, name, functionName, slot, subscriptionId, apiVersion, functionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **functionName** | **String**| Function name. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **functionEnvelope** | [**FunctionEnvelope**](FunctionEnvelope.md)| Function details. | 

### Return type

[**FunctionEnvelope**](FunctionEnvelope.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateInstanceMSDeployOperation

> MSDeployStatus webAppsCreateInstanceMSDeployOperation(resourceGroupName, name, instanceId, subscriptionId, apiVersion, mSDeploy)

Invoke the MSDeploy web app extension.

Invoke the MSDeploy web app extension.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let instanceId = "instanceId_example"; // String | ID of web app instance.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let mSDeploy = new WebAppsApiClient.MSDeploy(); // MSDeploy | Details of MSDeploy operation
apiInstance.webAppsCreateInstanceMSDeployOperation(resourceGroupName, name, instanceId, subscriptionId, apiVersion, mSDeploy, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **instanceId** | **String**| ID of web app instance. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **mSDeploy** | [**MSDeploy**](MSDeploy.md)| Details of MSDeploy operation | 

### Return type

[**MSDeployStatus**](MSDeployStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateInstanceMSDeployOperationSlot

> MSDeployStatus webAppsCreateInstanceMSDeployOperationSlot(resourceGroupName, name, slot, instanceId, subscriptionId, apiVersion, mSDeploy)

Invoke the MSDeploy web app extension.

Invoke the MSDeploy web app extension.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let instanceId = "instanceId_example"; // String | ID of web app instance.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let mSDeploy = new WebAppsApiClient.MSDeploy(); // MSDeploy | Details of MSDeploy operation
apiInstance.webAppsCreateInstanceMSDeployOperationSlot(resourceGroupName, name, slot, instanceId, subscriptionId, apiVersion, mSDeploy, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **instanceId** | **String**| ID of web app instance. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **mSDeploy** | [**MSDeploy**](MSDeploy.md)| Details of MSDeploy operation | 

### Return type

[**MSDeployStatus**](MSDeployStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateMSDeployOperation

> MSDeployStatus webAppsCreateMSDeployOperation(resourceGroupName, name, subscriptionId, apiVersion, mSDeploy)

Invoke the MSDeploy web app extension.

Invoke the MSDeploy web app extension.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let mSDeploy = new WebAppsApiClient.MSDeploy(); // MSDeploy | Details of MSDeploy operation
apiInstance.webAppsCreateMSDeployOperation(resourceGroupName, name, subscriptionId, apiVersion, mSDeploy, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **mSDeploy** | [**MSDeploy**](MSDeploy.md)| Details of MSDeploy operation | 

### Return type

[**MSDeployStatus**](MSDeployStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateMSDeployOperationSlot

> MSDeployStatus webAppsCreateMSDeployOperationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, mSDeploy)

Invoke the MSDeploy web app extension.

Invoke the MSDeploy web app extension.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let mSDeploy = new WebAppsApiClient.MSDeploy(); // MSDeploy | Details of MSDeploy operation
apiInstance.webAppsCreateMSDeployOperationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, mSDeploy, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **mSDeploy** | [**MSDeploy**](MSDeploy.md)| Details of MSDeploy operation | 

### Return type

[**MSDeployStatus**](MSDeployStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdate

> WebAppsGet200Response webAppsCreateOrUpdate(resourceGroupName, name, subscriptionId, apiVersion, siteEnvelope)

Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Unique name of the app to create or update. To create or update a deployment slot, use the {slot} parameter.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteEnvelope = new WebAppsApiClient.WebAppsGet200Response(); // WebAppsGet200Response | A JSON representation of the app properties. See example.
apiInstance.webAppsCreateOrUpdate(resourceGroupName, name, subscriptionId, apiVersion, siteEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Unique name of the app to create or update. To create or update a deployment slot, use the {slot} parameter. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteEnvelope** | [**WebAppsGet200Response**](WebAppsGet200Response.md)| A JSON representation of the app properties. See example. | 

### Return type

[**WebAppsGet200Response**](WebAppsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateConfiguration

> SiteConfigResource webAppsCreateOrUpdateConfiguration(resourceGroupName, name, subscriptionId, apiVersion, siteConfig)

Updates the configuration of an app.

Updates the configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteConfig = new WebAppsApiClient.SiteConfigResource(); // SiteConfigResource | JSON representation of a SiteConfig object. See example.
apiInstance.webAppsCreateOrUpdateConfiguration(resourceGroupName, name, subscriptionId, apiVersion, siteConfig, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteConfig** | [**SiteConfigResource**](SiteConfigResource.md)| JSON representation of a SiteConfig object. See example. | 

### Return type

[**SiteConfigResource**](SiteConfigResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateConfigurationSlot

> SiteConfigResource webAppsCreateOrUpdateConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteConfig)

Updates the configuration of an app.

Updates the configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will update configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteConfig = new WebAppsApiClient.SiteConfigResource(); // SiteConfigResource | JSON representation of a SiteConfig object. See example.
apiInstance.webAppsCreateOrUpdateConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteConfig, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will update configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteConfig** | [**SiteConfigResource**](SiteConfigResource.md)| JSON representation of a SiteConfig object. See example. | 

### Return type

[**SiteConfigResource**](SiteConfigResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateDomainOwnershipIdentifier

> WebAppsGetDomainOwnershipIdentifier200Response webAppsCreateOrUpdateDomainOwnershipIdentifier(resourceGroupName, name, domainOwnershipIdentifierName, subscriptionId, apiVersion, domainOwnershipIdentifier)

Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let domainOwnershipIdentifierName = "domainOwnershipIdentifierName_example"; // String | Name of domain ownership identifier.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let domainOwnershipIdentifier = new WebAppsApiClient.WebAppsGetDomainOwnershipIdentifier200Response(); // WebAppsGetDomainOwnershipIdentifier200Response | A JSON representation of the domain ownership properties.
apiInstance.webAppsCreateOrUpdateDomainOwnershipIdentifier(resourceGroupName, name, domainOwnershipIdentifierName, subscriptionId, apiVersion, domainOwnershipIdentifier, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **domainOwnershipIdentifierName** | **String**| Name of domain ownership identifier. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **domainOwnershipIdentifier** | [**WebAppsGetDomainOwnershipIdentifier200Response**](WebAppsGetDomainOwnershipIdentifier200Response.md)| A JSON representation of the domain ownership properties. | 

### Return type

[**WebAppsGetDomainOwnershipIdentifier200Response**](WebAppsGetDomainOwnershipIdentifier200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateDomainOwnershipIdentifierSlot

> WebAppsGetDomainOwnershipIdentifier200Response webAppsCreateOrUpdateDomainOwnershipIdentifierSlot(resourceGroupName, name, domainOwnershipIdentifierName, slot, subscriptionId, apiVersion, domainOwnershipIdentifier)

Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let domainOwnershipIdentifierName = "domainOwnershipIdentifierName_example"; // String | Name of domain ownership identifier.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let domainOwnershipIdentifier = new WebAppsApiClient.WebAppsGetDomainOwnershipIdentifier200Response(); // WebAppsGetDomainOwnershipIdentifier200Response | A JSON representation of the domain ownership properties.
apiInstance.webAppsCreateOrUpdateDomainOwnershipIdentifierSlot(resourceGroupName, name, domainOwnershipIdentifierName, slot, subscriptionId, apiVersion, domainOwnershipIdentifier, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **domainOwnershipIdentifierName** | **String**| Name of domain ownership identifier. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **domainOwnershipIdentifier** | [**WebAppsGetDomainOwnershipIdentifier200Response**](WebAppsGetDomainOwnershipIdentifier200Response.md)| A JSON representation of the domain ownership properties. | 

### Return type

[**WebAppsGetDomainOwnershipIdentifier200Response**](WebAppsGetDomainOwnershipIdentifier200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateFunctionSecret

> KeyInfo webAppsCreateOrUpdateFunctionSecret(resourceGroupName, name, functionName, keyName, subscriptionId, apiVersion, key)

Add or update a function secret.

Add or update a function secret.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let functionName = "functionName_example"; // String | The name of the function.
let keyName = "keyName_example"; // String | The name of the key.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let key = new WebAppsApiClient.KeyInfo(); // KeyInfo | The key to create or update
apiInstance.webAppsCreateOrUpdateFunctionSecret(resourceGroupName, name, functionName, keyName, subscriptionId, apiVersion, key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **functionName** | **String**| The name of the function. | 
 **keyName** | **String**| The name of the key. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **key** | [**KeyInfo**](KeyInfo.md)| The key to create or update | 

### Return type

[**KeyInfo**](KeyInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateFunctionSecretSlot

> KeyInfo webAppsCreateOrUpdateFunctionSecretSlot(resourceGroupName, name, functionName, keyName, slot, subscriptionId, apiVersion, key)

Add or update a function secret.

Add or update a function secret.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let functionName = "functionName_example"; // String | The name of the function.
let keyName = "keyName_example"; // String | The name of the key.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let key = new WebAppsApiClient.KeyInfo(); // KeyInfo | The key to create or update
apiInstance.webAppsCreateOrUpdateFunctionSecretSlot(resourceGroupName, name, functionName, keyName, slot, subscriptionId, apiVersion, key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **functionName** | **String**| The name of the function. | 
 **keyName** | **String**| The name of the key. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **key** | [**KeyInfo**](KeyInfo.md)| The key to create or update | 

### Return type

[**KeyInfo**](KeyInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateHostNameBinding

> HostNameBinding webAppsCreateOrUpdateHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion, hostNameBinding)

Creates a hostname binding for an app.

Creates a hostname binding for an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let hostName = "hostName_example"; // String | Hostname in the hostname binding.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let hostNameBinding = new WebAppsApiClient.HostNameBinding(); // HostNameBinding | Binding details. This is the JSON representation of a HostNameBinding object.
apiInstance.webAppsCreateOrUpdateHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion, hostNameBinding, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **hostName** | **String**| Hostname in the hostname binding. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **hostNameBinding** | [**HostNameBinding**](HostNameBinding.md)| Binding details. This is the JSON representation of a HostNameBinding object. | 

### Return type

[**HostNameBinding**](HostNameBinding.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateHostNameBindingSlot

> HostNameBinding webAppsCreateOrUpdateHostNameBindingSlot(resourceGroupName, name, hostName, slot, subscriptionId, apiVersion, hostNameBinding)

Creates a hostname binding for an app.

Creates a hostname binding for an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let hostName = "hostName_example"; // String | Hostname in the hostname binding.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will create a binding for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let hostNameBinding = new WebAppsApiClient.HostNameBinding(); // HostNameBinding | Binding details. This is the JSON representation of a HostNameBinding object.
apiInstance.webAppsCreateOrUpdateHostNameBindingSlot(resourceGroupName, name, hostName, slot, subscriptionId, apiVersion, hostNameBinding, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **hostName** | **String**| Hostname in the hostname binding. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will create a binding for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **hostNameBinding** | [**HostNameBinding**](HostNameBinding.md)| Binding details. This is the JSON representation of a HostNameBinding object. | 

### Return type

[**HostNameBinding**](HostNameBinding.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateHostSecret

> KeyInfo webAppsCreateOrUpdateHostSecret(resourceGroupName, name, keyType, keyName, subscriptionId, apiVersion, key)

Add or update a host level secret.

Add or update a host level secret.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let keyType = "keyType_example"; // String | The type of host key.
let keyName = "keyName_example"; // String | The name of the key.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let key = new WebAppsApiClient.KeyInfo(); // KeyInfo | The key to create or update
apiInstance.webAppsCreateOrUpdateHostSecret(resourceGroupName, name, keyType, keyName, subscriptionId, apiVersion, key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **keyType** | **String**| The type of host key. | 
 **keyName** | **String**| The name of the key. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **key** | [**KeyInfo**](KeyInfo.md)| The key to create or update | 

### Return type

[**KeyInfo**](KeyInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateHostSecretSlot

> KeyInfo webAppsCreateOrUpdateHostSecretSlot(resourceGroupName, name, keyType, keyName, slot, subscriptionId, apiVersion, key)

Add or update a host level secret.

Add or update a host level secret.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let keyType = "keyType_example"; // String | The type of host key.
let keyName = "keyName_example"; // String | The name of the key.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let key = new WebAppsApiClient.KeyInfo(); // KeyInfo | The key to create or update
apiInstance.webAppsCreateOrUpdateHostSecretSlot(resourceGroupName, name, keyType, keyName, slot, subscriptionId, apiVersion, key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **keyType** | **String**| The type of host key. | 
 **keyName** | **String**| The name of the key. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **key** | [**KeyInfo**](KeyInfo.md)| The key to create or update | 

### Return type

[**KeyInfo**](KeyInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateHybridConnection

> WebAppsGetHybridConnection200Response webAppsCreateOrUpdateHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion, connectionEnvelope)

Creates a new Hybrid Connection using a Service Bus relay.

Creates a new Hybrid Connection using a Service Bus relay.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let namespaceName = "namespaceName_example"; // String | The namespace for this hybrid connection.
let relayName = "relayName_example"; // String | The relay name for this hybrid connection.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.WebAppsGetHybridConnection200Response(); // WebAppsGetHybridConnection200Response | The details of the hybrid connection.
apiInstance.webAppsCreateOrUpdateHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **namespaceName** | **String**| The namespace for this hybrid connection. | 
 **relayName** | **String**| The relay name for this hybrid connection. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**WebAppsGetHybridConnection200Response**](WebAppsGetHybridConnection200Response.md)| The details of the hybrid connection. | 

### Return type

[**WebAppsGetHybridConnection200Response**](WebAppsGetHybridConnection200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateHybridConnectionSlot

> WebAppsGetHybridConnection200Response webAppsCreateOrUpdateHybridConnectionSlot(resourceGroupName, name, namespaceName, relayName, slot, subscriptionId, apiVersion, connectionEnvelope)

Creates a new Hybrid Connection using a Service Bus relay.

Creates a new Hybrid Connection using a Service Bus relay.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let namespaceName = "namespaceName_example"; // String | The namespace for this hybrid connection.
let relayName = "relayName_example"; // String | The relay name for this hybrid connection.
let slot = "slot_example"; // String | The name of the slot for the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.WebAppsGetHybridConnection200Response(); // WebAppsGetHybridConnection200Response | The details of the hybrid connection.
apiInstance.webAppsCreateOrUpdateHybridConnectionSlot(resourceGroupName, name, namespaceName, relayName, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **namespaceName** | **String**| The namespace for this hybrid connection. | 
 **relayName** | **String**| The relay name for this hybrid connection. | 
 **slot** | **String**| The name of the slot for the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**WebAppsGetHybridConnection200Response**](WebAppsGetHybridConnection200Response.md)| The details of the hybrid connection. | 

### Return type

[**WebAppsGetHybridConnection200Response**](WebAppsGetHybridConnection200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdatePublicCertificate

> PublicCertificate webAppsCreateOrUpdatePublicCertificate(resourceGroupName, name, publicCertificateName, subscriptionId, apiVersion, publicCertificate)

Creates a hostname binding for an app.

Creates a hostname binding for an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let publicCertificateName = "publicCertificateName_example"; // String | Public certificate name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let publicCertificate = new WebAppsApiClient.PublicCertificate(); // PublicCertificate | Public certificate details. This is the JSON representation of a PublicCertificate object.
apiInstance.webAppsCreateOrUpdatePublicCertificate(resourceGroupName, name, publicCertificateName, subscriptionId, apiVersion, publicCertificate, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **publicCertificateName** | **String**| Public certificate name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **publicCertificate** | [**PublicCertificate**](PublicCertificate.md)| Public certificate details. This is the JSON representation of a PublicCertificate object. | 

### Return type

[**PublicCertificate**](PublicCertificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdatePublicCertificateSlot

> PublicCertificate webAppsCreateOrUpdatePublicCertificateSlot(resourceGroupName, name, publicCertificateName, slot, subscriptionId, apiVersion, publicCertificate)

Creates a hostname binding for an app.

Creates a hostname binding for an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let publicCertificateName = "publicCertificateName_example"; // String | Public certificate name.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will create a binding for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let publicCertificate = new WebAppsApiClient.PublicCertificate(); // PublicCertificate | Public certificate details. This is the JSON representation of a PublicCertificate object.
apiInstance.webAppsCreateOrUpdatePublicCertificateSlot(resourceGroupName, name, publicCertificateName, slot, subscriptionId, apiVersion, publicCertificate, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **publicCertificateName** | **String**| Public certificate name. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will create a binding for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **publicCertificate** | [**PublicCertificate**](PublicCertificate.md)| Public certificate details. This is the JSON representation of a PublicCertificate object. | 

### Return type

[**PublicCertificate**](PublicCertificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateRelayServiceConnection

> RelayServiceConnectionEntity webAppsCreateOrUpdateRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, connectionEnvelope)

Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let entityName = "entityName_example"; // String | Name of the hybrid connection configuration.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.RelayServiceConnectionEntity(); // RelayServiceConnectionEntity | Details of the hybrid connection configuration.
apiInstance.webAppsCreateOrUpdateRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **entityName** | **String**| Name of the hybrid connection configuration. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)| Details of the hybrid connection configuration. | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateRelayServiceConnectionSlot

> RelayServiceConnectionEntity webAppsCreateOrUpdateRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, connectionEnvelope)

Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let entityName = "entityName_example"; // String | Name of the hybrid connection configuration.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will create or update a hybrid connection for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.RelayServiceConnectionEntity(); // RelayServiceConnectionEntity | Details of the hybrid connection configuration.
apiInstance.webAppsCreateOrUpdateRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **entityName** | **String**| Name of the hybrid connection configuration. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will create or update a hybrid connection for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)| Details of the hybrid connection configuration. | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateSlot

> WebAppsGet200Response webAppsCreateOrUpdateSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteEnvelope)

Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Unique name of the app to create or update. To create or update a deployment slot, use the {slot} parameter.
let slot = "slot_example"; // String | Name of the deployment slot to create or update. By default, this API attempts to create or modify the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteEnvelope = new WebAppsApiClient.WebAppsGet200Response(); // WebAppsGet200Response | A JSON representation of the app properties. See example.
apiInstance.webAppsCreateOrUpdateSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Unique name of the app to create or update. To create or update a deployment slot, use the {slot} parameter. | 
 **slot** | **String**| Name of the deployment slot to create or update. By default, this API attempts to create or modify the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteEnvelope** | [**WebAppsGet200Response**](WebAppsGet200Response.md)| A JSON representation of the app properties. See example. | 

### Return type

[**WebAppsGet200Response**](WebAppsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateSourceControl

> SiteSourceControl webAppsCreateOrUpdateSourceControl(resourceGroupName, name, subscriptionId, apiVersion, siteSourceControl)

Updates the source control configuration of an app.

Updates the source control configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteSourceControl = new WebAppsApiClient.SiteSourceControl(); // SiteSourceControl | JSON representation of a SiteSourceControl object. See example.
apiInstance.webAppsCreateOrUpdateSourceControl(resourceGroupName, name, subscriptionId, apiVersion, siteSourceControl, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteSourceControl** | [**SiteSourceControl**](SiteSourceControl.md)| JSON representation of a SiteSourceControl object. See example. | 

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateSourceControlSlot

> SiteSourceControl webAppsCreateOrUpdateSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteSourceControl)

Updates the source control configuration of an app.

Updates the source control configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will update the source control configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteSourceControl = new WebAppsApiClient.SiteSourceControl(); // SiteSourceControl | JSON representation of a SiteSourceControl object. See example.
apiInstance.webAppsCreateOrUpdateSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteSourceControl, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will update the source control configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteSourceControl** | [**SiteSourceControl**](SiteSourceControl.md)| JSON representation of a SiteSourceControl object. See example. | 

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateSwiftVirtualNetworkConnection

> SwiftVirtualNetwork webAppsCreateOrUpdateSwiftVirtualNetworkConnection(resourceGroupName, name, subscriptionId, apiVersion, connectionEnvelope)

Integrates this Web App with a Virtual Network. This requires that 1) \&quot;swiftSupported\&quot; is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not  in use by another App Service Plan other than the one this App is in.

Integrates this Web App with a Virtual Network. This requires that 1) \&quot;swiftSupported\&quot; is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.SwiftVirtualNetwork(); // SwiftVirtualNetwork | Properties of the Virtual Network connection. See example.
apiInstance.webAppsCreateOrUpdateSwiftVirtualNetworkConnection(resourceGroupName, name, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**SwiftVirtualNetwork**](SwiftVirtualNetwork.md)| Properties of the Virtual Network connection. See example. | 

### Return type

[**SwiftVirtualNetwork**](SwiftVirtualNetwork.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateSwiftVirtualNetworkConnectionSlot

> SwiftVirtualNetwork webAppsCreateOrUpdateSwiftVirtualNetworkConnectionSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, connectionEnvelope)

Integrates this Web App with a Virtual Network. This requires that 1) \&quot;swiftSupported\&quot; is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not  in use by another App Service Plan other than the one this App is in.

Integrates this Web App with a Virtual Network. This requires that 1) \&quot;swiftSupported\&quot; is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will add or update connections for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.SwiftVirtualNetwork(); // SwiftVirtualNetwork | Properties of the Virtual Network connection. See example.
apiInstance.webAppsCreateOrUpdateSwiftVirtualNetworkConnectionSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will add or update connections for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**SwiftVirtualNetwork**](SwiftVirtualNetwork.md)| Properties of the Virtual Network connection. See example. | 

### Return type

[**SwiftVirtualNetwork**](SwiftVirtualNetwork.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateVnetConnection

> WebAppsGetVnetConnectionSlot200Response webAppsCreateOrUpdateVnetConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, connectionEnvelope)

Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let vnetName = "vnetName_example"; // String | Name of an existing Virtual Network.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.WebAppsGetVnetConnectionSlot200Response(); // WebAppsGetVnetConnectionSlot200Response | Properties of the Virtual Network connection. See example.
apiInstance.webAppsCreateOrUpdateVnetConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **vnetName** | **String**| Name of an existing Virtual Network. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**WebAppsGetVnetConnectionSlot200Response**](WebAppsGetVnetConnectionSlot200Response.md)| Properties of the Virtual Network connection. See example. | 

### Return type

[**WebAppsGetVnetConnectionSlot200Response**](WebAppsGetVnetConnectionSlot200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateVnetConnectionGateway

> WebAppsGetVnetConnectionGatewaySlot200Response webAppsCreateOrUpdateVnetConnectionGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope)

Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let vnetName = "vnetName_example"; // String | Name of the Virtual Network.
let gatewayName = "gatewayName_example"; // String | Name of the gateway. Currently, the only supported string is \"primary\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.WebAppsGetVnetConnectionGatewaySlot200Response(); // WebAppsGetVnetConnectionGatewaySlot200Response | The properties to update this gateway with.
apiInstance.webAppsCreateOrUpdateVnetConnectionGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **vnetName** | **String**| Name of the Virtual Network. | 
 **gatewayName** | **String**| Name of the gateway. Currently, the only supported string is \&quot;primary\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**WebAppsGetVnetConnectionGatewaySlot200Response**](WebAppsGetVnetConnectionGatewaySlot200Response.md)| The properties to update this gateway with. | 

### Return type

[**WebAppsGetVnetConnectionGatewaySlot200Response**](WebAppsGetVnetConnectionGatewaySlot200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateVnetConnectionGatewaySlot

> WebAppsGetVnetConnectionGatewaySlot200Response webAppsCreateOrUpdateVnetConnectionGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion, connectionEnvelope)

Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let vnetName = "vnetName_example"; // String | Name of the Virtual Network.
let gatewayName = "gatewayName_example"; // String | Name of the gateway. Currently, the only supported string is \"primary\".
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will add or update a gateway for the production slot's Virtual Network.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.WebAppsGetVnetConnectionGatewaySlot200Response(); // WebAppsGetVnetConnectionGatewaySlot200Response | The properties to update this gateway with.
apiInstance.webAppsCreateOrUpdateVnetConnectionGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **vnetName** | **String**| Name of the Virtual Network. | 
 **gatewayName** | **String**| Name of the gateway. Currently, the only supported string is \&quot;primary\&quot;. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will add or update a gateway for the production slot&#39;s Virtual Network. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**WebAppsGetVnetConnectionGatewaySlot200Response**](WebAppsGetVnetConnectionGatewaySlot200Response.md)| The properties to update this gateway with. | 

### Return type

[**WebAppsGetVnetConnectionGatewaySlot200Response**](WebAppsGetVnetConnectionGatewaySlot200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsCreateOrUpdateVnetConnectionSlot

> WebAppsGetVnetConnectionSlot200Response webAppsCreateOrUpdateVnetConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, connectionEnvelope)

Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let vnetName = "vnetName_example"; // String | Name of an existing Virtual Network.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will add or update connections for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.WebAppsGetVnetConnectionSlot200Response(); // WebAppsGetVnetConnectionSlot200Response | Properties of the Virtual Network connection. See example.
apiInstance.webAppsCreateOrUpdateVnetConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **vnetName** | **String**| Name of an existing Virtual Network. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will add or update connections for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**WebAppsGetVnetConnectionSlot200Response**](WebAppsGetVnetConnectionSlot200Response.md)| Properties of the Virtual Network connection. See example. | 

### Return type

[**WebAppsGetVnetConnectionSlot200Response**](WebAppsGetVnetConnectionSlot200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsDelete

> webAppsDelete(resourceGroupName, name, subscriptionId, apiVersion, opts)

Deletes a web, mobile, or API app, or one of the deployment slots.

Deletes a web, mobile, or API app, or one of the deployment slots.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app to delete.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'deleteMetrics': true, // Boolean | If true, web app metrics are also deleted.
  'deleteEmptyServerFarm': true // Boolean | Specify false if you want to keep empty App Service plan. By default, empty App Service plan is deleted.
};
apiInstance.webAppsDelete(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app to delete. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **deleteMetrics** | **Boolean**| If true, web app metrics are also deleted. | [optional] 
 **deleteEmptyServerFarm** | **Boolean**| Specify false if you want to keep empty App Service plan. By default, empty App Service plan is deleted. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteBackup

> webAppsDeleteBackup(resourceGroupName, name, backupId, subscriptionId, apiVersion)

Deletes a backup of an app by its ID.

Deletes a backup of an app by its ID.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let backupId = "backupId_example"; // String | ID of the backup.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteBackup(resourceGroupName, name, backupId, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **backupId** | **String**| ID of the backup. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteBackupConfiguration

> webAppsDeleteBackupConfiguration(resourceGroupName, name, subscriptionId, apiVersion)

Deletes the backup configuration of an app.

Deletes the backup configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteBackupConfiguration(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteBackupConfigurationSlot

> webAppsDeleteBackupConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Deletes the backup configuration of an app.

Deletes the backup configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will delete the backup configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteBackupConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will delete the backup configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteBackupSlot

> webAppsDeleteBackupSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion)

Deletes a backup of an app by its ID.

Deletes a backup of an app by its ID.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let backupId = "backupId_example"; // String | ID of the backup.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will delete a backup of the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteBackupSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **backupId** | **String**| ID of the backup. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will delete a backup of the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteContinuousWebJob

> webAppsDeleteContinuousWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion)

Delete a continuous web job by its ID for an app, or a deployment slot.

Delete a continuous web job by its ID for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteContinuousWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteContinuousWebJobSlot

> webAppsDeleteContinuousWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion)

Delete a continuous web job by its ID for an app, or a deployment slot.

Delete a continuous web job by its ID for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteContinuousWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteDeployment

> webAppsDeleteDeployment(resourceGroupName, name, id, subscriptionId, apiVersion)

Delete a deployment by its ID for an app, or a deployment slot.

Delete a deployment by its ID for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let id = "id_example"; // String | Deployment ID.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteDeployment(resourceGroupName, name, id, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **id** | **String**| Deployment ID. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteDeploymentSlot

> webAppsDeleteDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion)

Delete a deployment by its ID for an app, or a deployment slot.

Delete a deployment by its ID for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let id = "id_example"; // String | Deployment ID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **id** | **String**| Deployment ID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteDomainOwnershipIdentifier

> webAppsDeleteDomainOwnershipIdentifier(resourceGroupName, name, domainOwnershipIdentifierName, subscriptionId, apiVersion)

Deletes a domain ownership identifier for a web app.

Deletes a domain ownership identifier for a web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let domainOwnershipIdentifierName = "domainOwnershipIdentifierName_example"; // String | Name of domain ownership identifier.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteDomainOwnershipIdentifier(resourceGroupName, name, domainOwnershipIdentifierName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **domainOwnershipIdentifierName** | **String**| Name of domain ownership identifier. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteDomainOwnershipIdentifierSlot

> webAppsDeleteDomainOwnershipIdentifierSlot(resourceGroupName, name, domainOwnershipIdentifierName, slot, subscriptionId, apiVersion)

Deletes a domain ownership identifier for a web app.

Deletes a domain ownership identifier for a web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let domainOwnershipIdentifierName = "domainOwnershipIdentifierName_example"; // String | Name of domain ownership identifier.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteDomainOwnershipIdentifierSlot(resourceGroupName, name, domainOwnershipIdentifierName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **domainOwnershipIdentifierName** | **String**| Name of domain ownership identifier. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteFunction

> webAppsDeleteFunction(resourceGroupName, name, functionName, subscriptionId, apiVersion)

Delete a function for web site, or a deployment slot.

Delete a function for web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let functionName = "functionName_example"; // String | Function name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteFunction(resourceGroupName, name, functionName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **functionName** | **String**| Function name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteFunctionSecret

> webAppsDeleteFunctionSecret(resourceGroupName, name, functionName, keyName, subscriptionId, apiVersion)

Delete a function secret.

Delete a function secret.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let functionName = "functionName_example"; // String | The name of the function.
let keyName = "keyName_example"; // String | The name of the key.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteFunctionSecret(resourceGroupName, name, functionName, keyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **functionName** | **String**| The name of the function. | 
 **keyName** | **String**| The name of the key. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteFunctionSecretSlot

> webAppsDeleteFunctionSecretSlot(resourceGroupName, name, functionName, keyName, slot, subscriptionId, apiVersion)

Delete a function secret.

Delete a function secret.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let functionName = "functionName_example"; // String | The name of the function.
let keyName = "keyName_example"; // String | The name of the key.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteFunctionSecretSlot(resourceGroupName, name, functionName, keyName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **functionName** | **String**| The name of the function. | 
 **keyName** | **String**| The name of the key. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteHostNameBinding

> webAppsDeleteHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion)

Deletes a hostname binding for an app.

Deletes a hostname binding for an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let hostName = "hostName_example"; // String | Hostname in the hostname binding.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **hostName** | **String**| Hostname in the hostname binding. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteHostNameBindingSlot

> webAppsDeleteHostNameBindingSlot(resourceGroupName, name, slot, hostName, subscriptionId, apiVersion)

Deletes a hostname binding for an app.

Deletes a hostname binding for an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
let hostName = "hostName_example"; // String | Hostname in the hostname binding.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteHostNameBindingSlot(resourceGroupName, name, slot, hostName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot. | 
 **hostName** | **String**| Hostname in the hostname binding. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteHostSecret

> webAppsDeleteHostSecret(resourceGroupName, name, keyType, keyName, subscriptionId, apiVersion)

Delete a host level secret.

Delete a host level secret.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let keyType = "keyType_example"; // String | The type of host key.
let keyName = "keyName_example"; // String | The name of the key.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteHostSecret(resourceGroupName, name, keyType, keyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **keyType** | **String**| The type of host key. | 
 **keyName** | **String**| The name of the key. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsDeleteHostSecretSlot

> webAppsDeleteHostSecretSlot(resourceGroupName, name, keyType, keyName, slot, subscriptionId, apiVersion)

Delete a host level secret.

Delete a host level secret.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let keyType = "keyType_example"; // String | The type of host key.
let keyName = "keyName_example"; // String | The name of the key.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteHostSecretSlot(resourceGroupName, name, keyType, keyName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **keyType** | **String**| The type of host key. | 
 **keyName** | **String**| The name of the key. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsDeleteHybridConnection

> webAppsDeleteHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion)

Removes a Hybrid Connection from this site.

Removes a Hybrid Connection from this site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let namespaceName = "namespaceName_example"; // String | The namespace for this hybrid connection.
let relayName = "relayName_example"; // String | The relay name for this hybrid connection.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **namespaceName** | **String**| The namespace for this hybrid connection. | 
 **relayName** | **String**| The relay name for this hybrid connection. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteHybridConnectionSlot

> webAppsDeleteHybridConnectionSlot(resourceGroupName, name, namespaceName, relayName, slot, subscriptionId, apiVersion)

Removes a Hybrid Connection from this site.

Removes a Hybrid Connection from this site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let namespaceName = "namespaceName_example"; // String | The namespace for this hybrid connection.
let relayName = "relayName_example"; // String | The relay name for this hybrid connection.
let slot = "slot_example"; // String | The name of the slot for the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteHybridConnectionSlot(resourceGroupName, name, namespaceName, relayName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **namespaceName** | **String**| The namespace for this hybrid connection. | 
 **relayName** | **String**| The relay name for this hybrid connection. | 
 **slot** | **String**| The name of the slot for the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteInstanceFunctionSlot

> webAppsDeleteInstanceFunctionSlot(resourceGroupName, name, functionName, slot, subscriptionId, apiVersion)

Delete a function for web site, or a deployment slot.

Delete a function for web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let functionName = "functionName_example"; // String | Function name.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteInstanceFunctionSlot(resourceGroupName, name, functionName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **functionName** | **String**| Function name. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteInstanceProcess

> webAppsDeleteInstanceProcess(resourceGroupName, name, processId, instanceId, subscriptionId, apiVersion)

Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteInstanceProcess(resourceGroupName, name, processId, instanceId, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteInstanceProcessSlot

> webAppsDeleteInstanceProcessSlot(resourceGroupName, name, processId, slot, instanceId, subscriptionId, apiVersion)

Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteInstanceProcessSlot(resourceGroupName, name, processId, slot, instanceId, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeletePremierAddOn

> webAppsDeletePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion)

Delete a premier add-on from an app.

Delete a premier add-on from an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let premierAddOnName = "premierAddOnName_example"; // String | Add-on name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeletePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **premierAddOnName** | **String**| Add-on name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeletePremierAddOnSlot

> webAppsDeletePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion)

Delete a premier add-on from an app.

Delete a premier add-on from an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let premierAddOnName = "premierAddOnName_example"; // String | Add-on name.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will delete the named add-on for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeletePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **premierAddOnName** | **String**| Add-on name. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will delete the named add-on for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteProcess

> webAppsDeleteProcess(resourceGroupName, name, processId, subscriptionId, apiVersion)

Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteProcess(resourceGroupName, name, processId, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteProcessSlot

> webAppsDeleteProcessSlot(resourceGroupName, name, processId, slot, subscriptionId, apiVersion)

Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteProcessSlot(resourceGroupName, name, processId, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeletePublicCertificate

> webAppsDeletePublicCertificate(resourceGroupName, name, publicCertificateName, subscriptionId, apiVersion)

Deletes a hostname binding for an app.

Deletes a hostname binding for an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let publicCertificateName = "publicCertificateName_example"; // String | Public certificate name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeletePublicCertificate(resourceGroupName, name, publicCertificateName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **publicCertificateName** | **String**| Public certificate name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeletePublicCertificateSlot

> webAppsDeletePublicCertificateSlot(resourceGroupName, name, slot, publicCertificateName, subscriptionId, apiVersion)

Deletes a hostname binding for an app.

Deletes a hostname binding for an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
let publicCertificateName = "publicCertificateName_example"; // String | Public certificate name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeletePublicCertificateSlot(resourceGroupName, name, slot, publicCertificateName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot. | 
 **publicCertificateName** | **String**| Public certificate name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteRelayServiceConnection

> webAppsDeleteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion)

Deletes a relay service connection by its name.

Deletes a relay service connection by its name.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let entityName = "entityName_example"; // String | Name of the hybrid connection configuration.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **entityName** | **String**| Name of the hybrid connection configuration. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteRelayServiceConnectionSlot

> webAppsDeleteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion)

Deletes a relay service connection by its name.

Deletes a relay service connection by its name.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let entityName = "entityName_example"; // String | Name of the hybrid connection configuration.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will delete a hybrid connection for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **entityName** | **String**| Name of the hybrid connection configuration. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will delete a hybrid connection for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteSiteExtension

> webAppsDeleteSiteExtension(resourceGroupName, name, siteExtensionId, subscriptionId, apiVersion)

Remove a site extension from a web site, or a deployment slot.

Remove a site extension from a web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let siteExtensionId = "siteExtensionId_example"; // String | Site extension name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteSiteExtension(resourceGroupName, name, siteExtensionId, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **siteExtensionId** | **String**| Site extension name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteSiteExtensionSlot

> webAppsDeleteSiteExtensionSlot(resourceGroupName, name, siteExtensionId, slot, subscriptionId, apiVersion)

Remove a site extension from a web site, or a deployment slot.

Remove a site extension from a web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let siteExtensionId = "siteExtensionId_example"; // String | Site extension name.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteSiteExtensionSlot(resourceGroupName, name, siteExtensionId, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **siteExtensionId** | **String**| Site extension name. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteSlot

> webAppsDeleteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts)

Deletes a web, mobile, or API app, or one of the deployment slots.

Deletes a web, mobile, or API app, or one of the deployment slots.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app to delete.
let slot = "slot_example"; // String | Name of the deployment slot to delete. By default, the API deletes the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'deleteMetrics': true, // Boolean | If true, web app metrics are also deleted.
  'deleteEmptyServerFarm': true // Boolean | Specify true if the App Service plan will be empty after app deletion and you want to delete the empty App Service plan. By default, the empty App Service plan is not deleted.
};
apiInstance.webAppsDeleteSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app to delete. | 
 **slot** | **String**| Name of the deployment slot to delete. By default, the API deletes the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **deleteMetrics** | **Boolean**| If true, web app metrics are also deleted. | [optional] 
 **deleteEmptyServerFarm** | **Boolean**| Specify true if the App Service plan will be empty after app deletion and you want to delete the empty App Service plan. By default, the empty App Service plan is not deleted. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteSourceControl

> webAppsDeleteSourceControl(resourceGroupName, name, subscriptionId, apiVersion)

Deletes the source control configuration of an app.

Deletes the source control configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteSourceControl(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteSourceControlSlot

> webAppsDeleteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Deletes the source control configuration of an app.

Deletes the source control configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will delete the source control configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will delete the source control configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteSwiftVirtualNetwork

> webAppsDeleteSwiftVirtualNetwork(resourceGroupName, name, subscriptionId, apiVersion)

Deletes a Swift Virtual Network connection from an app (or deployment slot).

Deletes a Swift Virtual Network connection from an app (or deployment slot).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteSwiftVirtualNetwork(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteSwiftVirtualNetworkSlot

> webAppsDeleteSwiftVirtualNetworkSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Deletes a Swift Virtual Network connection from an app (or deployment slot).

Deletes a Swift Virtual Network connection from an app (or deployment slot).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will delete the connection for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteSwiftVirtualNetworkSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will delete the connection for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteTriggeredWebJob

> webAppsDeleteTriggeredWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion)

Delete a triggered web job by its ID for an app, or a deployment slot.

Delete a triggered web job by its ID for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteTriggeredWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteTriggeredWebJobSlot

> webAppsDeleteTriggeredWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion)

Delete a triggered web job by its ID for an app, or a deployment slot.

Delete a triggered web job by its ID for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteTriggeredWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteVnetConnection

> webAppsDeleteVnetConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion)

Deletes a connection from an app (or deployment slot to a named virtual network.

Deletes a connection from an app (or deployment slot to a named virtual network.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let vnetName = "vnetName_example"; // String | Name of the virtual network.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteVnetConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **vnetName** | **String**| Name of the virtual network. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDeleteVnetConnectionSlot

> webAppsDeleteVnetConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion)

Deletes a connection from an app (or deployment slot to a named virtual network.

Deletes a connection from an app (or deployment slot to a named virtual network.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let vnetName = "vnetName_example"; // String | Name of the virtual network.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will delete the connection for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsDeleteVnetConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **vnetName** | **String**| Name of the virtual network. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will delete the connection for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsDiscoverBackup

> RestoreRequest webAppsDiscoverBackup(resourceGroupName, name, subscriptionId, apiVersion, request)

Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup.

Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebAppsApiClient.RestoreRequest(); // RestoreRequest | A RestoreRequest object that includes Azure storage URL and blog name for discovery of backup.
apiInstance.webAppsDiscoverBackup(resourceGroupName, name, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **request** | [**RestoreRequest**](RestoreRequest.md)| A RestoreRequest object that includes Azure storage URL and blog name for discovery of backup. | 

### Return type

[**RestoreRequest**](RestoreRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsDiscoverBackupSlot

> RestoreRequest webAppsDiscoverBackupSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request)

Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup.

Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will perform discovery for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebAppsApiClient.RestoreRequest(); // RestoreRequest | A RestoreRequest object that includes Azure storage URL and blog name for discovery of backup.
apiInstance.webAppsDiscoverBackupSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will perform discovery for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **request** | [**RestoreRequest**](RestoreRequest.md)| A RestoreRequest object that includes Azure storage URL and blog name for discovery of backup. | 

### Return type

[**RestoreRequest**](RestoreRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsGenerateNewSitePublishingPassword

> webAppsGenerateNewSitePublishingPassword(resourceGroupName, name, subscriptionId, apiVersion)

Generates a new publishing password for an app (or deployment slot, if specified).

Generates a new publishing password for an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGenerateNewSitePublishingPassword(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsGenerateNewSitePublishingPasswordSlot

> webAppsGenerateNewSitePublishingPasswordSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Generates a new publishing password for an app (or deployment slot, if specified).

Generates a new publishing password for an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API generate a new publishing password for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGenerateNewSitePublishingPasswordSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API generate a new publishing password for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsGet

> WebAppsGet200Response webAppsGet(resourceGroupName, name, subscriptionId, apiVersion)

Gets the details of a web, mobile, or API app.

Gets the details of a web, mobile, or API app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGet(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsGet200Response**](WebAppsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetAuthSettings

> SiteAuthSettings webAppsGetAuthSettings(resourceGroupName, name, subscriptionId, apiVersion)

Gets the Authentication/Authorization settings of an app.

Gets the Authentication/Authorization settings of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetAuthSettings(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteAuthSettings**](SiteAuthSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetAuthSettingsSlot

> SiteAuthSettings webAppsGetAuthSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the Authentication/Authorization settings of an app.

Gets the Authentication/Authorization settings of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get the settings for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetAuthSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get the settings for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteAuthSettings**](SiteAuthSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetBackupConfiguration

> BackupRequest webAppsGetBackupConfiguration(resourceGroupName, name, subscriptionId, apiVersion)

Gets the backup configuration of an app.

Gets the backup configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetBackupConfiguration(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**BackupRequest**](BackupRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetBackupConfigurationSlot

> BackupRequest webAppsGetBackupConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the backup configuration of an app.

Gets the backup configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get the backup configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetBackupConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get the backup configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**BackupRequest**](BackupRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetBackupStatus

> BackupItem webAppsGetBackupStatus(resourceGroupName, name, backupId, subscriptionId, apiVersion)

Gets a backup of an app by its ID.

Gets a backup of an app by its ID.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let backupId = "backupId_example"; // String | ID of the backup.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetBackupStatus(resourceGroupName, name, backupId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **backupId** | **String**| ID of the backup. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetBackupStatusSlot

> BackupItem webAppsGetBackupStatusSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion)

Gets a backup of an app by its ID.

Gets a backup of an app by its ID.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let backupId = "backupId_example"; // String | ID of the backup.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get a backup of the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetBackupStatusSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **backupId** | **String**| ID of the backup. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get a backup of the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetConfiguration

> SiteConfigResource webAppsGetConfiguration(resourceGroupName, name, subscriptionId, apiVersion)

Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.

Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetConfiguration(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteConfigResource**](SiteConfigResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetConfigurationSlot

> SiteConfigResource webAppsGetConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.

Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteConfigResource**](SiteConfigResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetConfigurationSnapshot

> SiteConfigResource webAppsGetConfigurationSnapshot(resourceGroupName, name, snapshotId, subscriptionId, apiVersion)

Gets a snapshot of the configuration of an app at a previous point in time.

Gets a snapshot of the configuration of an app at a previous point in time.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let snapshotId = "snapshotId_example"; // String | The ID of the snapshot to read.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetConfigurationSnapshot(resourceGroupName, name, snapshotId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **snapshotId** | **String**| The ID of the snapshot to read. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteConfigResource**](SiteConfigResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetConfigurationSnapshotSlot

> SiteConfigResource webAppsGetConfigurationSnapshotSlot(resourceGroupName, name, snapshotId, slot, subscriptionId, apiVersion)

Gets a snapshot of the configuration of an app at a previous point in time.

Gets a snapshot of the configuration of an app at a previous point in time.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let snapshotId = "snapshotId_example"; // String | The ID of the snapshot to read.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetConfigurationSnapshotSlot(resourceGroupName, name, snapshotId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **snapshotId** | **String**| The ID of the snapshot to read. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteConfigResource**](SiteConfigResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetContainerLogsZip

> File webAppsGetContainerLogsZip(resourceGroupName, name, subscriptionId, apiVersion)

Gets the ZIP archived docker log files for the given site

Gets the ZIP archived docker log files for the given site

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetContainerLogsZip(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/zip


## webAppsGetContainerLogsZipSlot

> File webAppsGetContainerLogsZipSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the ZIP archived docker log files for the given site

Gets the ZIP archived docker log files for the given site

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetContainerLogsZipSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/zip


## webAppsGetContinuousWebJob

> ContinuousWebJob webAppsGetContinuousWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion)

Gets a continuous web job by its ID for an app, or a deployment slot.

Gets a continuous web job by its ID for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetContinuousWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ContinuousWebJob**](ContinuousWebJob.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetContinuousWebJobSlot

> ContinuousWebJob webAppsGetContinuousWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion)

Gets a continuous web job by its ID for an app, or a deployment slot.

Gets a continuous web job by its ID for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetContinuousWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ContinuousWebJob**](ContinuousWebJob.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetDeployment

> Deployment webAppsGetDeployment(resourceGroupName, name, id, subscriptionId, apiVersion)

Get a deployment by its ID for an app, or a deployment slot.

Get a deployment by its ID for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let id = "id_example"; // String | Deployment ID.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetDeployment(resourceGroupName, name, id, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **id** | **String**| Deployment ID. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetDeploymentSlot

> Deployment webAppsGetDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion)

Get a deployment by its ID for an app, or a deployment slot.

Get a deployment by its ID for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let id = "id_example"; // String | Deployment ID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API gets a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetDeploymentSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **id** | **String**| Deployment ID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API gets a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetDiagnosticLogsConfiguration

> SiteLogsConfig webAppsGetDiagnosticLogsConfiguration(resourceGroupName, name, subscriptionId, apiVersion)

Gets the logging configuration of an app.

Gets the logging configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetDiagnosticLogsConfiguration(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteLogsConfig**](SiteLogsConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetDiagnosticLogsConfigurationSlot

> SiteLogsConfig webAppsGetDiagnosticLogsConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the logging configuration of an app.

Gets the logging configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get the logging configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetDiagnosticLogsConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get the logging configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteLogsConfig**](SiteLogsConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetDomainOwnershipIdentifier

> WebAppsGetDomainOwnershipIdentifier200Response webAppsGetDomainOwnershipIdentifier(resourceGroupName, name, domainOwnershipIdentifierName, subscriptionId, apiVersion)

Get domain ownership identifier for web app.

Get domain ownership identifier for web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let domainOwnershipIdentifierName = "domainOwnershipIdentifierName_example"; // String | Name of domain ownership identifier.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetDomainOwnershipIdentifier(resourceGroupName, name, domainOwnershipIdentifierName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **domainOwnershipIdentifierName** | **String**| Name of domain ownership identifier. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsGetDomainOwnershipIdentifier200Response**](WebAppsGetDomainOwnershipIdentifier200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetDomainOwnershipIdentifierSlot

> WebAppsGetDomainOwnershipIdentifier200Response webAppsGetDomainOwnershipIdentifierSlot(resourceGroupName, name, domainOwnershipIdentifierName, slot, subscriptionId, apiVersion)

Get domain ownership identifier for web app.

Get domain ownership identifier for web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let domainOwnershipIdentifierName = "domainOwnershipIdentifierName_example"; // String | Name of domain ownership identifier.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetDomainOwnershipIdentifierSlot(resourceGroupName, name, domainOwnershipIdentifierName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **domainOwnershipIdentifierName** | **String**| Name of domain ownership identifier. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsGetDomainOwnershipIdentifier200Response**](WebAppsGetDomainOwnershipIdentifier200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetFunction

> FunctionEnvelope webAppsGetFunction(resourceGroupName, name, functionName, subscriptionId, apiVersion)

Get function information by its ID for web site, or a deployment slot.

Get function information by its ID for web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let functionName = "functionName_example"; // String | Function name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetFunction(resourceGroupName, name, functionName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **functionName** | **String**| Function name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**FunctionEnvelope**](FunctionEnvelope.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetFunctionsAdminToken

> String webAppsGetFunctionsAdminToken(resourceGroupName, name, subscriptionId, apiVersion)

Fetch a short lived token that can be exchanged for a master key.

Fetch a short lived token that can be exchanged for a master key.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetFunctionsAdminToken(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetFunctionsAdminTokenSlot

> String webAppsGetFunctionsAdminTokenSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Fetch a short lived token that can be exchanged for a master key.

Fetch a short lived token that can be exchanged for a master key.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetFunctionsAdminTokenSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetHostNameBinding

> HostNameBinding webAppsGetHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion)

Get the named hostname binding for an app (or deployment slot, if specified).

Get the named hostname binding for an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let hostName = "hostName_example"; // String | Hostname in the hostname binding.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetHostNameBinding(resourceGroupName, name, hostName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **hostName** | **String**| Hostname in the hostname binding. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostNameBinding**](HostNameBinding.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetHostNameBindingSlot

> HostNameBinding webAppsGetHostNameBindingSlot(resourceGroupName, name, slot, hostName, subscriptionId, apiVersion)

Get the named hostname binding for an app (or deployment slot, if specified).

Get the named hostname binding for an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API the named binding for the production slot.
let hostName = "hostName_example"; // String | Hostname in the hostname binding.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetHostNameBindingSlot(resourceGroupName, name, slot, hostName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API the named binding for the production slot. | 
 **hostName** | **String**| Hostname in the hostname binding. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostNameBinding**](HostNameBinding.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetHybridConnection

> WebAppsGetHybridConnection200Response webAppsGetHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion)

Retrieves a specific Service Bus Hybrid Connection used by this Web App.

Retrieves a specific Service Bus Hybrid Connection used by this Web App.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let namespaceName = "namespaceName_example"; // String | The namespace for this hybrid connection.
let relayName = "relayName_example"; // String | The relay name for this hybrid connection.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **namespaceName** | **String**| The namespace for this hybrid connection. | 
 **relayName** | **String**| The relay name for this hybrid connection. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsGetHybridConnection200Response**](WebAppsGetHybridConnection200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetHybridConnectionSlot

> WebAppsGetHybridConnection200Response webAppsGetHybridConnectionSlot(resourceGroupName, name, namespaceName, relayName, slot, subscriptionId, apiVersion)

Retrieves a specific Service Bus Hybrid Connection used by this Web App.

Retrieves a specific Service Bus Hybrid Connection used by this Web App.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let namespaceName = "namespaceName_example"; // String | The namespace for this hybrid connection.
let relayName = "relayName_example"; // String | The relay name for this hybrid connection.
let slot = "slot_example"; // String | The name of the slot for the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetHybridConnectionSlot(resourceGroupName, name, namespaceName, relayName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **namespaceName** | **String**| The namespace for this hybrid connection. | 
 **relayName** | **String**| The relay name for this hybrid connection. | 
 **slot** | **String**| The name of the slot for the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsGetHybridConnection200Response**](WebAppsGetHybridConnection200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetInstanceFunctionSlot

> FunctionEnvelope webAppsGetInstanceFunctionSlot(resourceGroupName, name, functionName, slot, subscriptionId, apiVersion)

Get function information by its ID for web site, or a deployment slot.

Get function information by its ID for web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let functionName = "functionName_example"; // String | Function name.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetInstanceFunctionSlot(resourceGroupName, name, functionName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **functionName** | **String**| Function name. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**FunctionEnvelope**](FunctionEnvelope.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetInstanceMSDeployLog

> MSDeployLog webAppsGetInstanceMSDeployLog(resourceGroupName, name, instanceId, subscriptionId, apiVersion)

Get the MSDeploy Log for the last MSDeploy operation.

Get the MSDeploy Log for the last MSDeploy operation.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let instanceId = "instanceId_example"; // String | ID of web app instance.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetInstanceMSDeployLog(resourceGroupName, name, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **instanceId** | **String**| ID of web app instance. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MSDeployLog**](MSDeployLog.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetInstanceMSDeployLogSlot

> MSDeployLog webAppsGetInstanceMSDeployLogSlot(resourceGroupName, name, slot, instanceId, subscriptionId, apiVersion)

Get the MSDeploy Log for the last MSDeploy operation.

Get the MSDeploy Log for the last MSDeploy operation.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let instanceId = "instanceId_example"; // String | ID of web app instance.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetInstanceMSDeployLogSlot(resourceGroupName, name, slot, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **instanceId** | **String**| ID of web app instance. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MSDeployLog**](MSDeployLog.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetInstanceMsDeployStatus

> MSDeployStatus webAppsGetInstanceMsDeployStatus(resourceGroupName, name, instanceId, subscriptionId, apiVersion)

Get the status of the last MSDeploy operation.

Get the status of the last MSDeploy operation.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let instanceId = "instanceId_example"; // String | ID of web app instance.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetInstanceMsDeployStatus(resourceGroupName, name, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **instanceId** | **String**| ID of web app instance. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MSDeployStatus**](MSDeployStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetInstanceMsDeployStatusSlot

> MSDeployStatus webAppsGetInstanceMsDeployStatusSlot(resourceGroupName, name, slot, instanceId, subscriptionId, apiVersion)

Get the status of the last MSDeploy operation.

Get the status of the last MSDeploy operation.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let instanceId = "instanceId_example"; // String | ID of web app instance.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetInstanceMsDeployStatusSlot(resourceGroupName, name, slot, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **instanceId** | **String**| ID of web app instance. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MSDeployStatus**](MSDeployStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetInstanceProcess

> ProcessInfo webAppsGetInstanceProcess(resourceGroupName, name, processId, instanceId, subscriptionId, apiVersion)

Get process information by its ID for a specific scaled-out instance in a web site.

Get process information by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetInstanceProcess(resourceGroupName, name, processId, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessInfo**](ProcessInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetInstanceProcessDump

> File webAppsGetInstanceProcessDump(resourceGroupName, name, processId, instanceId, subscriptionId, apiVersion)

Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetInstanceProcessDump(resourceGroupName, name, processId, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetInstanceProcessDumpSlot

> File webAppsGetInstanceProcessDumpSlot(resourceGroupName, name, processId, slot, instanceId, subscriptionId, apiVersion)

Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetInstanceProcessDumpSlot(resourceGroupName, name, processId, slot, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetInstanceProcessModule

> ProcessModuleInfo webAppsGetInstanceProcessModule(resourceGroupName, name, processId, baseAddress, instanceId, subscriptionId, apiVersion)

Get process information by its ID for a specific scaled-out instance in a web site.

Get process information by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let baseAddress = "baseAddress_example"; // String | Module base address.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetInstanceProcessModule(resourceGroupName, name, processId, baseAddress, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **baseAddress** | **String**| Module base address. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessModuleInfo**](ProcessModuleInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetInstanceProcessModuleSlot

> ProcessModuleInfo webAppsGetInstanceProcessModuleSlot(resourceGroupName, name, processId, baseAddress, slot, instanceId, subscriptionId, apiVersion)

Get process information by its ID for a specific scaled-out instance in a web site.

Get process information by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let baseAddress = "baseAddress_example"; // String | Module base address.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetInstanceProcessModuleSlot(resourceGroupName, name, processId, baseAddress, slot, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **baseAddress** | **String**| Module base address. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessModuleInfo**](ProcessModuleInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetInstanceProcessSlot

> ProcessInfo webAppsGetInstanceProcessSlot(resourceGroupName, name, processId, slot, instanceId, subscriptionId, apiVersion)

Get process information by its ID for a specific scaled-out instance in a web site.

Get process information by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetInstanceProcessSlot(resourceGroupName, name, processId, slot, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessInfo**](ProcessInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetInstanceProcessThread

> ProcessThreadInfo webAppsGetInstanceProcessThread(resourceGroupName, name, processId, threadId, instanceId, subscriptionId, apiVersion)

Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let threadId = "threadId_example"; // String | TID.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetInstanceProcessThread(resourceGroupName, name, processId, threadId, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **threadId** | **String**| TID. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessThreadInfo**](ProcessThreadInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetInstanceProcessThreadSlot

> ProcessThreadInfo webAppsGetInstanceProcessThreadSlot(resourceGroupName, name, processId, threadId, slot, instanceId, subscriptionId, apiVersion)

Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let threadId = "threadId_example"; // String | TID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetInstanceProcessThreadSlot(resourceGroupName, name, processId, threadId, slot, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **threadId** | **String**| TID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessThreadInfo**](ProcessThreadInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetMSDeployLog

> MSDeployLog webAppsGetMSDeployLog(resourceGroupName, name, subscriptionId, apiVersion)

Get the MSDeploy Log for the last MSDeploy operation.

Get the MSDeploy Log for the last MSDeploy operation.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetMSDeployLog(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MSDeployLog**](MSDeployLog.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetMSDeployLogSlot

> MSDeployLog webAppsGetMSDeployLogSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Get the MSDeploy Log for the last MSDeploy operation.

Get the MSDeploy Log for the last MSDeploy operation.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetMSDeployLogSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MSDeployLog**](MSDeployLog.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetMSDeployStatus

> MSDeployStatus webAppsGetMSDeployStatus(resourceGroupName, name, subscriptionId, apiVersion)

Get the status of the last MSDeploy operation.

Get the status of the last MSDeploy operation.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetMSDeployStatus(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MSDeployStatus**](MSDeployStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetMSDeployStatusSlot

> MSDeployStatus webAppsGetMSDeployStatusSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Get the status of the last MSDeploy operation.

Get the status of the last MSDeploy operation.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetMSDeployStatusSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MSDeployStatus**](MSDeployStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetMigrateMySqlStatus

> MigrateMySqlStatus webAppsGetMigrateMySqlStatus(resourceGroupName, name, subscriptionId, apiVersion)

Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled

Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetMigrateMySqlStatus(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MigrateMySqlStatus**](MigrateMySqlStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetMigrateMySqlStatusSlot

> MigrateMySqlStatus webAppsGetMigrateMySqlStatusSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled

Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetMigrateMySqlStatusSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**MigrateMySqlStatus**](MigrateMySqlStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetNetworkTraceOperation

> [NetworkTrace] webAppsGetNetworkTraceOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion)

Gets a named operation for a network trace capturing (or deployment slot, if specified).

Gets a named operation for a network trace capturing (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let operationId = "operationId_example"; // String | GUID of the operation.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetNetworkTraceOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **operationId** | **String**| GUID of the operation. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[NetworkTrace]**](NetworkTrace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetNetworkTraceOperationSlot

> [NetworkTrace] webAppsGetNetworkTraceOperationSlot(resourceGroupName, name, operationId, slot, subscriptionId, apiVersion)

Gets a named operation for a network trace capturing (or deployment slot, if specified).

Gets a named operation for a network trace capturing (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let operationId = "operationId_example"; // String | GUID of the operation.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get an operation for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetNetworkTraceOperationSlot(resourceGroupName, name, operationId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **operationId** | **String**| GUID of the operation. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get an operation for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[NetworkTrace]**](NetworkTrace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetNetworkTraceOperationSlotV2

> [NetworkTrace] webAppsGetNetworkTraceOperationSlotV2(resourceGroupName, name, operationId, slot, subscriptionId, apiVersion)

Gets a named operation for a network trace capturing (or deployment slot, if specified).

Gets a named operation for a network trace capturing (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let operationId = "operationId_example"; // String | GUID of the operation.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get an operation for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetNetworkTraceOperationSlotV2(resourceGroupName, name, operationId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **operationId** | **String**| GUID of the operation. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get an operation for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[NetworkTrace]**](NetworkTrace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetNetworkTraceOperationV2

> [NetworkTrace] webAppsGetNetworkTraceOperationV2(resourceGroupName, name, operationId, subscriptionId, apiVersion)

Gets a named operation for a network trace capturing (or deployment slot, if specified).

Gets a named operation for a network trace capturing (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let operationId = "operationId_example"; // String | GUID of the operation.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetNetworkTraceOperationV2(resourceGroupName, name, operationId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **operationId** | **String**| GUID of the operation. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[NetworkTrace]**](NetworkTrace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetNetworkTraces

> [NetworkTrace] webAppsGetNetworkTraces(resourceGroupName, name, operationId, subscriptionId, apiVersion)

Gets a named operation for a network trace capturing (or deployment slot, if specified).

Gets a named operation for a network trace capturing (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let operationId = "operationId_example"; // String | GUID of the operation.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetNetworkTraces(resourceGroupName, name, operationId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **operationId** | **String**| GUID of the operation. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[NetworkTrace]**](NetworkTrace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetNetworkTracesSlot

> [NetworkTrace] webAppsGetNetworkTracesSlot(resourceGroupName, name, operationId, slot, subscriptionId, apiVersion)

Gets a named operation for a network trace capturing (or deployment slot, if specified).

Gets a named operation for a network trace capturing (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let operationId = "operationId_example"; // String | GUID of the operation.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get an operation for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetNetworkTracesSlot(resourceGroupName, name, operationId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **operationId** | **String**| GUID of the operation. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get an operation for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[NetworkTrace]**](NetworkTrace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetNetworkTracesSlotV2

> [NetworkTrace] webAppsGetNetworkTracesSlotV2(resourceGroupName, name, operationId, slot, subscriptionId, apiVersion)

Gets a named operation for a network trace capturing (or deployment slot, if specified).

Gets a named operation for a network trace capturing (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let operationId = "operationId_example"; // String | GUID of the operation.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get an operation for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetNetworkTracesSlotV2(resourceGroupName, name, operationId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **operationId** | **String**| GUID of the operation. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get an operation for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[NetworkTrace]**](NetworkTrace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetNetworkTracesV2

> [NetworkTrace] webAppsGetNetworkTracesV2(resourceGroupName, name, operationId, subscriptionId, apiVersion)

Gets a named operation for a network trace capturing (or deployment slot, if specified).

Gets a named operation for a network trace capturing (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let operationId = "operationId_example"; // String | GUID of the operation.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetNetworkTracesV2(resourceGroupName, name, operationId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **operationId** | **String**| GUID of the operation. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[NetworkTrace]**](NetworkTrace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetPremierAddOn

> PremierAddOn webAppsGetPremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion)

Gets a named add-on of an app.

Gets a named add-on of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let premierAddOnName = "premierAddOnName_example"; // String | Add-on name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetPremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **premierAddOnName** | **String**| Add-on name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**PremierAddOn**](PremierAddOn.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetPremierAddOnSlot

> PremierAddOn webAppsGetPremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion)

Gets a named add-on of an app.

Gets a named add-on of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let premierAddOnName = "premierAddOnName_example"; // String | Add-on name.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get the named add-on for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetPremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **premierAddOnName** | **String**| Add-on name. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get the named add-on for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**PremierAddOn**](PremierAddOn.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetPrivateAccess

> PrivateAccess webAppsGetPrivateAccess(resourceGroupName, name, subscriptionId, apiVersion)

Gets data around private site access enablement and authorized Virtual Networks that can access the site.

Gets data around private site access enablement and authorized Virtual Networks that can access the site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetPrivateAccess(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**PrivateAccess**](PrivateAccess.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetPrivateAccessSlot

> PrivateAccess webAppsGetPrivateAccessSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets data around private site access enablement and authorized Virtual Networks that can access the site.

Gets data around private site access enablement and authorized Virtual Networks that can access the site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let slot = "slot_example"; // String | The name of the slot for the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetPrivateAccessSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **slot** | **String**| The name of the slot for the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**PrivateAccess**](PrivateAccess.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetProcess

> ProcessInfo webAppsGetProcess(resourceGroupName, name, processId, subscriptionId, apiVersion)

Get process information by its ID for a specific scaled-out instance in a web site.

Get process information by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetProcess(resourceGroupName, name, processId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessInfo**](ProcessInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetProcessDump

> File webAppsGetProcessDump(resourceGroupName, name, processId, subscriptionId, apiVersion)

Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetProcessDump(resourceGroupName, name, processId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetProcessDumpSlot

> File webAppsGetProcessDumpSlot(resourceGroupName, name, processId, slot, subscriptionId, apiVersion)

Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetProcessDumpSlot(resourceGroupName, name, processId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetProcessModule

> ProcessModuleInfo webAppsGetProcessModule(resourceGroupName, name, processId, baseAddress, subscriptionId, apiVersion)

Get process information by its ID for a specific scaled-out instance in a web site.

Get process information by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let baseAddress = "baseAddress_example"; // String | Module base address.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetProcessModule(resourceGroupName, name, processId, baseAddress, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **baseAddress** | **String**| Module base address. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessModuleInfo**](ProcessModuleInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetProcessModuleSlot

> ProcessModuleInfo webAppsGetProcessModuleSlot(resourceGroupName, name, processId, baseAddress, slot, subscriptionId, apiVersion)

Get process information by its ID for a specific scaled-out instance in a web site.

Get process information by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let baseAddress = "baseAddress_example"; // String | Module base address.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetProcessModuleSlot(resourceGroupName, name, processId, baseAddress, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **baseAddress** | **String**| Module base address. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessModuleInfo**](ProcessModuleInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetProcessSlot

> ProcessInfo webAppsGetProcessSlot(resourceGroupName, name, processId, slot, subscriptionId, apiVersion)

Get process information by its ID for a specific scaled-out instance in a web site.

Get process information by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetProcessSlot(resourceGroupName, name, processId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessInfo**](ProcessInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetProcessThread

> ProcessThreadInfo webAppsGetProcessThread(resourceGroupName, name, processId, threadId, subscriptionId, apiVersion)

Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let threadId = "threadId_example"; // String | TID.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetProcessThread(resourceGroupName, name, processId, threadId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **threadId** | **String**| TID. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessThreadInfo**](ProcessThreadInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetProcessThreadSlot

> ProcessThreadInfo webAppsGetProcessThreadSlot(resourceGroupName, name, processId, threadId, slot, subscriptionId, apiVersion)

Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let threadId = "threadId_example"; // String | TID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetProcessThreadSlot(resourceGroupName, name, processId, threadId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **threadId** | **String**| TID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessThreadInfo**](ProcessThreadInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetPublicCertificate

> PublicCertificate webAppsGetPublicCertificate(resourceGroupName, name, publicCertificateName, subscriptionId, apiVersion)

Get the named public certificate for an app (or deployment slot, if specified).

Get the named public certificate for an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let publicCertificateName = "publicCertificateName_example"; // String | Public certificate name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetPublicCertificate(resourceGroupName, name, publicCertificateName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **publicCertificateName** | **String**| Public certificate name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**PublicCertificate**](PublicCertificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetPublicCertificateSlot

> PublicCertificate webAppsGetPublicCertificateSlot(resourceGroupName, name, slot, publicCertificateName, subscriptionId, apiVersion)

Get the named public certificate for an app (or deployment slot, if specified).

Get the named public certificate for an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API the named binding for the production slot.
let publicCertificateName = "publicCertificateName_example"; // String | Public certificate name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetPublicCertificateSlot(resourceGroupName, name, slot, publicCertificateName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API the named binding for the production slot. | 
 **publicCertificateName** | **String**| Public certificate name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**PublicCertificate**](PublicCertificate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetRelayServiceConnection

> RelayServiceConnectionEntity webAppsGetRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion)

Gets a hybrid connection configuration by its name.

Gets a hybrid connection configuration by its name.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let entityName = "entityName_example"; // String | Name of the hybrid connection.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **entityName** | **String**| Name of the hybrid connection. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetRelayServiceConnectionSlot

> RelayServiceConnectionEntity webAppsGetRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion)

Gets a hybrid connection configuration by its name.

Gets a hybrid connection configuration by its name.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let entityName = "entityName_example"; // String | Name of the hybrid connection.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get a hybrid connection for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **entityName** | **String**| Name of the hybrid connection. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get a hybrid connection for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetSiteExtension

> SiteExtensionInfo webAppsGetSiteExtension(resourceGroupName, name, siteExtensionId, subscriptionId, apiVersion)

Get site extension information by its ID for a web site, or a deployment slot.

Get site extension information by its ID for a web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let siteExtensionId = "siteExtensionId_example"; // String | Site extension name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetSiteExtension(resourceGroupName, name, siteExtensionId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **siteExtensionId** | **String**| Site extension name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteExtensionInfo**](SiteExtensionInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetSiteExtensionSlot

> SiteExtensionInfo webAppsGetSiteExtensionSlot(resourceGroupName, name, siteExtensionId, slot, subscriptionId, apiVersion)

Get site extension information by its ID for a web site, or a deployment slot.

Get site extension information by its ID for a web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let siteExtensionId = "siteExtensionId_example"; // String | Site extension name.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetSiteExtensionSlot(resourceGroupName, name, siteExtensionId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **siteExtensionId** | **String**| Site extension name. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteExtensionInfo**](SiteExtensionInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetSitePhpErrorLogFlag

> SitePhpErrorLogFlag webAppsGetSitePhpErrorLogFlag(resourceGroupName, name, subscriptionId, apiVersion)

Gets web app&#39;s event logs.

Gets web app&#39;s event logs.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetSitePhpErrorLogFlag(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SitePhpErrorLogFlag**](SitePhpErrorLogFlag.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetSitePhpErrorLogFlagSlot

> SitePhpErrorLogFlag webAppsGetSitePhpErrorLogFlagSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets web app&#39;s event logs.

Gets web app&#39;s event logs.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetSitePhpErrorLogFlagSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SitePhpErrorLogFlag**](SitePhpErrorLogFlag.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetSlot

> WebAppsGet200Response webAppsGetSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the details of a web, mobile, or API app.

Gets the details of a web, mobile, or API app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. By default, this API returns the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. By default, this API returns the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsGet200Response**](WebAppsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetSourceControl

> SiteSourceControl webAppsGetSourceControl(resourceGroupName, name, subscriptionId, apiVersion)

Gets the source control configuration of an app.

Gets the source control configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetSourceControl(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetSourceControlSlot

> SiteSourceControl webAppsGetSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the source control configuration of an app.

Gets the source control configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get the source control configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get the source control configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetSwiftVirtualNetworkConnection

> SwiftVirtualNetwork webAppsGetSwiftVirtualNetworkConnection(resourceGroupName, name, subscriptionId, apiVersion)

Gets a Swift Virtual Network connection.

Gets a Swift Virtual Network connection.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetSwiftVirtualNetworkConnection(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SwiftVirtualNetwork**](SwiftVirtualNetwork.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetSwiftVirtualNetworkConnectionSlot

> SwiftVirtualNetwork webAppsGetSwiftVirtualNetworkConnectionSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets a Swift Virtual Network connection.

Gets a Swift Virtual Network connection.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get a gateway for the production slot's Virtual Network.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetSwiftVirtualNetworkConnectionSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get a gateway for the production slot&#39;s Virtual Network. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SwiftVirtualNetwork**](SwiftVirtualNetwork.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetTriggeredWebJob

> TriggeredWebJob webAppsGetTriggeredWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion)

Gets a triggered web job by its ID for an app, or a deployment slot.

Gets a triggered web job by its ID for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetTriggeredWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**TriggeredWebJob**](TriggeredWebJob.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetTriggeredWebJobHistory

> TriggeredJobHistory webAppsGetTriggeredWebJobHistory(resourceGroupName, name, webJobName, id, subscriptionId, apiVersion)

Gets a triggered web job&#39;s history by its ID for an app, , or a deployment slot.

Gets a triggered web job&#39;s history by its ID for an app, , or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let id = "id_example"; // String | History ID.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetTriggeredWebJobHistory(resourceGroupName, name, webJobName, id, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **id** | **String**| History ID. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**TriggeredJobHistory**](TriggeredJobHistory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetTriggeredWebJobHistorySlot

> TriggeredJobHistory webAppsGetTriggeredWebJobHistorySlot(resourceGroupName, name, webJobName, id, slot, subscriptionId, apiVersion)

Gets a triggered web job&#39;s history by its ID for an app, , or a deployment slot.

Gets a triggered web job&#39;s history by its ID for an app, , or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let id = "id_example"; // String | History ID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetTriggeredWebJobHistorySlot(resourceGroupName, name, webJobName, id, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **id** | **String**| History ID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**TriggeredJobHistory**](TriggeredJobHistory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetTriggeredWebJobSlot

> TriggeredWebJob webAppsGetTriggeredWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion)

Gets a triggered web job by its ID for an app, or a deployment slot.

Gets a triggered web job by its ID for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetTriggeredWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**TriggeredWebJob**](TriggeredWebJob.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetVnetConnection

> WebAppsGetVnetConnectionSlot200Response webAppsGetVnetConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion)

Gets a virtual network the app (or deployment slot) is connected to by name.

Gets a virtual network the app (or deployment slot) is connected to by name.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let vnetName = "vnetName_example"; // String | Name of the virtual network.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetVnetConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **vnetName** | **String**| Name of the virtual network. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsGetVnetConnectionSlot200Response**](WebAppsGetVnetConnectionSlot200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetVnetConnectionGateway

> WebAppsGetVnetConnectionGatewaySlot200Response webAppsGetVnetConnectionGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion)

Gets an app&#39;s Virtual Network gateway.

Gets an app&#39;s Virtual Network gateway.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let vnetName = "vnetName_example"; // String | Name of the Virtual Network.
let gatewayName = "gatewayName_example"; // String | Name of the gateway. Currently, the only supported string is \"primary\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetVnetConnectionGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **vnetName** | **String**| Name of the Virtual Network. | 
 **gatewayName** | **String**| Name of the gateway. Currently, the only supported string is \&quot;primary\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsGetVnetConnectionGatewaySlot200Response**](WebAppsGetVnetConnectionGatewaySlot200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetVnetConnectionGatewaySlot

> WebAppsGetVnetConnectionGatewaySlot200Response webAppsGetVnetConnectionGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion)

Gets an app&#39;s Virtual Network gateway.

Gets an app&#39;s Virtual Network gateway.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let vnetName = "vnetName_example"; // String | Name of the Virtual Network.
let gatewayName = "gatewayName_example"; // String | Name of the gateway. Currently, the only supported string is \"primary\".
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get a gateway for the production slot's Virtual Network.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetVnetConnectionGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **vnetName** | **String**| Name of the Virtual Network. | 
 **gatewayName** | **String**| Name of the gateway. Currently, the only supported string is \&quot;primary\&quot;. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get a gateway for the production slot&#39;s Virtual Network. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsGetVnetConnectionGatewaySlot200Response**](WebAppsGetVnetConnectionGatewaySlot200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetVnetConnectionSlot

> WebAppsGetVnetConnectionSlot200Response webAppsGetVnetConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion)

Gets a virtual network the app (or deployment slot) is connected to by name.

Gets a virtual network the app (or deployment slot) is connected to by name.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let vnetName = "vnetName_example"; // String | Name of the virtual network.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get the named virtual network for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetVnetConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **vnetName** | **String**| Name of the virtual network. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get the named virtual network for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsGetVnetConnectionSlot200Response**](WebAppsGetVnetConnectionSlot200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetWebJob

> WebJob webAppsGetWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion)

Get webjob information for an app, or a deployment slot.

Get webjob information for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of the web job.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of the web job. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebJob**](WebJob.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetWebJobSlot

> WebJob webAppsGetWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion)

Get webjob information for an app, or a deployment slot.

Get webjob information for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of the web job.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of the web job. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebJob**](WebJob.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsGetWebSiteContainerLogs

> File webAppsGetWebSiteContainerLogs(resourceGroupName, name, subscriptionId, apiVersion)

Gets the last lines of docker logs for the given site

Gets the last lines of docker logs for the given site

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetWebSiteContainerLogs(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## webAppsGetWebSiteContainerLogsSlot

> File webAppsGetWebSiteContainerLogsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the last lines of docker logs for the given site

Gets the last lines of docker logs for the given site

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsGetWebSiteContainerLogsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## webAppsInstallSiteExtension

> SiteExtensionInfo webAppsInstallSiteExtension(resourceGroupName, name, siteExtensionId, subscriptionId, apiVersion)

Install site extension on a web site, or a deployment slot.

Install site extension on a web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let siteExtensionId = "siteExtensionId_example"; // String | Site extension name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsInstallSiteExtension(resourceGroupName, name, siteExtensionId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **siteExtensionId** | **String**| Site extension name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteExtensionInfo**](SiteExtensionInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsInstallSiteExtensionSlot

> SiteExtensionInfo webAppsInstallSiteExtensionSlot(resourceGroupName, name, siteExtensionId, slot, subscriptionId, apiVersion)

Install site extension on a web site, or a deployment slot.

Install site extension on a web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let siteExtensionId = "siteExtensionId_example"; // String | Site extension name.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsInstallSiteExtensionSlot(resourceGroupName, name, siteExtensionId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **siteExtensionId** | **String**| Site extension name. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteExtensionInfo**](SiteExtensionInfo.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsIsCloneable

> SiteCloneability webAppsIsCloneable(resourceGroupName, name, subscriptionId, apiVersion)

Shows whether an app can be cloned to another resource group or subscription.

Shows whether an app can be cloned to another resource group or subscription.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsIsCloneable(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteCloneability**](SiteCloneability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsIsCloneableSlot

> SiteCloneability webAppsIsCloneableSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Shows whether an app can be cloned to another resource group or subscription.

Shows whether an app can be cloned to another resource group or subscription.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. By default, this API returns information on the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsIsCloneableSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. By default, this API returns information on the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteCloneability**](SiteCloneability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsList

> WebAppsList200Response webAppsList(subscriptionId, apiVersion)

Get all apps for a subscription.

Get all apps for a subscription.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsList(subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsList200Response**](WebAppsList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListApplicationSettings

> StringDictionary webAppsListApplicationSettings(resourceGroupName, name, subscriptionId, apiVersion)

Gets the application settings of an app.

Gets the application settings of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListApplicationSettings(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListApplicationSettingsSlot

> StringDictionary webAppsListApplicationSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the application settings of an app.

Gets the application settings of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get the application settings for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListApplicationSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get the application settings for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListAzureStorageAccounts

> AzureStoragePropertyDictionaryResource webAppsListAzureStorageAccounts(resourceGroupName, name, subscriptionId, apiVersion)

Gets the Azure storage account configurations of an app.

Gets the Azure storage account configurations of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListAzureStorageAccounts(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AzureStoragePropertyDictionaryResource**](AzureStoragePropertyDictionaryResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListAzureStorageAccountsSlot

> AzureStoragePropertyDictionaryResource webAppsListAzureStorageAccountsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the Azure storage account configurations of an app.

Gets the Azure storage account configurations of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will update the Azure storage account configurations for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListAzureStorageAccountsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will update the Azure storage account configurations for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AzureStoragePropertyDictionaryResource**](AzureStoragePropertyDictionaryResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListBackupStatusSecrets

> BackupItem webAppsListBackupStatusSecrets(resourceGroupName, name, backupId, subscriptionId, apiVersion, request)

Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let backupId = "backupId_example"; // String | ID of backup.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebAppsApiClient.BackupRequest(); // BackupRequest | Information on backup request.
apiInstance.webAppsListBackupStatusSecrets(resourceGroupName, name, backupId, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **backupId** | **String**| ID of backup. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **request** | [**BackupRequest**](BackupRequest.md)| Information on backup request. | 

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsListBackupStatusSecretsSlot

> BackupItem webAppsListBackupStatusSecretsSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, request)

Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let backupId = "backupId_example"; // String | ID of backup.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebAppsApiClient.BackupRequest(); // BackupRequest | Information on backup request.
apiInstance.webAppsListBackupStatusSecretsSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **backupId** | **String**| ID of backup. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **request** | [**BackupRequest**](BackupRequest.md)| Information on backup request. | 

### Return type

[**BackupItem**](BackupItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsListBackups

> BackupItemCollection webAppsListBackups(resourceGroupName, name, subscriptionId, apiVersion)

Gets existing backups of an app.

Gets existing backups of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListBackups(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**BackupItemCollection**](BackupItemCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListBackupsSlot

> BackupItemCollection webAppsListBackupsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets existing backups of an app.

Gets existing backups of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get backups of the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListBackupsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get backups of the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**BackupItemCollection**](BackupItemCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListByResourceGroup

> WebAppsList200Response webAppsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, opts)

Gets all web, mobile, and API apps in the specified resource group.

Gets all web, mobile, and API apps in the specified resource group.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'includeSlots': true // Boolean | Specify <strong>true</strong> to include deployment slots in results. The default is false, which only gives you the production slot of all apps.
};
apiInstance.webAppsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **includeSlots** | **Boolean**| Specify &lt;strong&gt;true&lt;/strong&gt; to include deployment slots in results. The default is false, which only gives you the production slot of all apps. | [optional] 

### Return type

[**WebAppsList200Response**](WebAppsList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListConfigurationSnapshotInfo

> SiteConfigurationSnapshotInfoCollection webAppsListConfigurationSnapshotInfo(resourceGroupName, name, subscriptionId, apiVersion)

Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.

Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListConfigurationSnapshotInfo(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteConfigurationSnapshotInfoCollection**](SiteConfigurationSnapshotInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListConfigurationSnapshotInfoSlot

> SiteConfigurationSnapshotInfoCollection webAppsListConfigurationSnapshotInfoSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.

Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListConfigurationSnapshotInfoSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteConfigurationSnapshotInfoCollection**](SiteConfigurationSnapshotInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListConfigurations

> SiteConfigResourceCollection webAppsListConfigurations(resourceGroupName, name, subscriptionId, apiVersion)

List the configurations of an app

List the configurations of an app

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListConfigurations(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteConfigResourceCollection**](SiteConfigResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListConfigurationsSlot

> SiteConfigResourceCollection webAppsListConfigurationsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

List the configurations of an app

List the configurations of an app

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListConfigurationsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteConfigResourceCollection**](SiteConfigResourceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListConnectionStrings

> ConnectionStringDictionary webAppsListConnectionStrings(resourceGroupName, name, subscriptionId, apiVersion)

Gets the connection strings of an app.

Gets the connection strings of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListConnectionStrings(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ConnectionStringDictionary**](ConnectionStringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListConnectionStringsSlot

> ConnectionStringDictionary webAppsListConnectionStringsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the connection strings of an app.

Gets the connection strings of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get the connection settings for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListConnectionStringsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get the connection settings for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ConnectionStringDictionary**](ConnectionStringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListContinuousWebJobs

> ContinuousWebJobCollection webAppsListContinuousWebJobs(resourceGroupName, name, subscriptionId, apiVersion)

List continuous web jobs for an app, or a deployment slot.

List continuous web jobs for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListContinuousWebJobs(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ContinuousWebJobCollection**](ContinuousWebJobCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListContinuousWebJobsSlot

> ContinuousWebJobCollection webAppsListContinuousWebJobsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

List continuous web jobs for an app, or a deployment slot.

List continuous web jobs for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListContinuousWebJobsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ContinuousWebJobCollection**](ContinuousWebJobCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListDeploymentLog

> Deployment webAppsListDeploymentLog(resourceGroupName, name, id, subscriptionId, apiVersion)

List deployment log for specific deployment for an app, or a deployment slot.

List deployment log for specific deployment for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let id = "id_example"; // String | The ID of a specific deployment. This is the value of the name property in the JSON response from \"GET /api/sites/{siteName}/deployments\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListDeploymentLog(resourceGroupName, name, id, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **id** | **String**| The ID of a specific deployment. This is the value of the name property in the JSON response from \&quot;GET /api/sites/{siteName}/deployments\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListDeploymentLogSlot

> Deployment webAppsListDeploymentLogSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion)

List deployment log for specific deployment for an app, or a deployment slot.

List deployment log for specific deployment for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let id = "id_example"; // String | The ID of a specific deployment. This is the value of the name property in the JSON response from \"GET /api/sites/{siteName}/deployments\".
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListDeploymentLogSlot(resourceGroupName, name, id, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **id** | **String**| The ID of a specific deployment. This is the value of the name property in the JSON response from \&quot;GET /api/sites/{siteName}/deployments\&quot;. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListDeployments

> DeploymentCollection webAppsListDeployments(resourceGroupName, name, subscriptionId, apiVersion)

List deployments for an app, or a deployment slot.

List deployments for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListDeployments(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DeploymentCollection**](DeploymentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListDeploymentsSlot

> DeploymentCollection webAppsListDeploymentsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

List deployments for an app, or a deployment slot.

List deployments for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListDeploymentsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DeploymentCollection**](DeploymentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListDomainOwnershipIdentifiers

> WebAppsListDomainOwnershipIdentifiers200Response webAppsListDomainOwnershipIdentifiers(resourceGroupName, name, subscriptionId, apiVersion)

Lists ownership identifiers for domain associated with web app.

Lists ownership identifiers for domain associated with web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListDomainOwnershipIdentifiers(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsListDomainOwnershipIdentifiers200Response**](WebAppsListDomainOwnershipIdentifiers200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListDomainOwnershipIdentifiersSlot

> WebAppsListDomainOwnershipIdentifiers200Response webAppsListDomainOwnershipIdentifiersSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Lists ownership identifiers for domain associated with web app.

Lists ownership identifiers for domain associated with web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListDomainOwnershipIdentifiersSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsListDomainOwnershipIdentifiers200Response**](WebAppsListDomainOwnershipIdentifiers200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListFunctionKeys

> StringDictionary webAppsListFunctionKeys(resourceGroupName, name, functionName, subscriptionId, apiVersion)

Get function keys for a function in a web site, or a deployment slot.

Get function keys for a function in a web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let functionName = "functionName_example"; // String | Function name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListFunctionKeys(resourceGroupName, name, functionName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **functionName** | **String**| Function name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListFunctionKeysSlot

> StringDictionary webAppsListFunctionKeysSlot(resourceGroupName, name, functionName, slot, subscriptionId, apiVersion)

Get function keys for a function in a web site, or a deployment slot.

Get function keys for a function in a web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let functionName = "functionName_example"; // String | Function name.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListFunctionKeysSlot(resourceGroupName, name, functionName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **functionName** | **String**| Function name. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListFunctionSecrets

> FunctionSecrets webAppsListFunctionSecrets(resourceGroupName, name, functionName, subscriptionId, apiVersion)

Get function secrets for a function in a web site, or a deployment slot.

Get function secrets for a function in a web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let functionName = "functionName_example"; // String | Function name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListFunctionSecrets(resourceGroupName, name, functionName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **functionName** | **String**| Function name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**FunctionSecrets**](FunctionSecrets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListFunctionSecretsSlot

> FunctionSecrets webAppsListFunctionSecretsSlot(resourceGroupName, name, functionName, slot, subscriptionId, apiVersion)

Get function secrets for a function in a web site, or a deployment slot.

Get function secrets for a function in a web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let functionName = "functionName_example"; // String | Function name.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListFunctionSecretsSlot(resourceGroupName, name, functionName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **functionName** | **String**| Function name. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**FunctionSecrets**](FunctionSecrets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListFunctions

> FunctionEnvelopeCollection webAppsListFunctions(resourceGroupName, name, subscriptionId, apiVersion)

List the functions for a web site, or a deployment slot.

List the functions for a web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListFunctions(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**FunctionEnvelopeCollection**](FunctionEnvelopeCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListHostKeys

> HostKeys webAppsListHostKeys(resourceGroupName, name, subscriptionId, apiVersion)

Get host secrets for a function app.

Get host secrets for a function app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListHostKeys(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostKeys**](HostKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListHostKeysSlot

> HostKeys webAppsListHostKeysSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Get host secrets for a function app.

Get host secrets for a function app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListHostKeysSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostKeys**](HostKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListHostNameBindings

> HostNameBindingCollection webAppsListHostNameBindings(resourceGroupName, name, subscriptionId, apiVersion)

Get hostname bindings for an app or a deployment slot.

Get hostname bindings for an app or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListHostNameBindings(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostNameBindingCollection**](HostNameBindingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListHostNameBindingsSlot

> HostNameBindingCollection webAppsListHostNameBindingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Get hostname bindings for an app or a deployment slot.

Get hostname bindings for an app or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API gets hostname bindings for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListHostNameBindingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API gets hostname bindings for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostNameBindingCollection**](HostNameBindingCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListHybridConnectionKeys

> WebAppsListHybridConnectionKeys200Response webAppsListHybridConnectionKeys(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion)

Gets the send key name and value for a Hybrid Connection.

Gets the send key name and value for a Hybrid Connection.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let namespaceName = "namespaceName_example"; // String | The namespace for this hybrid connection.
let relayName = "relayName_example"; // String | The relay name for this hybrid connection.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListHybridConnectionKeys(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **namespaceName** | **String**| The namespace for this hybrid connection. | 
 **relayName** | **String**| The relay name for this hybrid connection. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsListHybridConnectionKeys200Response**](WebAppsListHybridConnectionKeys200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListHybridConnectionKeysSlot

> WebAppsListHybridConnectionKeys200Response webAppsListHybridConnectionKeysSlot(resourceGroupName, name, namespaceName, relayName, slot, subscriptionId, apiVersion)

Gets the send key name and value for a Hybrid Connection.

Gets the send key name and value for a Hybrid Connection.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let namespaceName = "namespaceName_example"; // String | The namespace for this hybrid connection.
let relayName = "relayName_example"; // String | The relay name for this hybrid connection.
let slot = "slot_example"; // String | The name of the slot for the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListHybridConnectionKeysSlot(resourceGroupName, name, namespaceName, relayName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **namespaceName** | **String**| The namespace for this hybrid connection. | 
 **relayName** | **String**| The relay name for this hybrid connection. | 
 **slot** | **String**| The name of the slot for the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsListHybridConnectionKeys200Response**](WebAppsListHybridConnectionKeys200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListHybridConnections

> WebAppsGetHybridConnection200Response webAppsListHybridConnections(resourceGroupName, name, subscriptionId, apiVersion)

Retrieves all Service Bus Hybrid Connections used by this Web App.

Retrieves all Service Bus Hybrid Connections used by this Web App.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListHybridConnections(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsGetHybridConnection200Response**](WebAppsGetHybridConnection200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListHybridConnectionsSlot

> WebAppsGetHybridConnection200Response webAppsListHybridConnectionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Retrieves all Service Bus Hybrid Connections used by this Web App.

Retrieves all Service Bus Hybrid Connections used by this Web App.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let slot = "slot_example"; // String | The name of the slot for the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListHybridConnectionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **slot** | **String**| The name of the slot for the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsGetHybridConnection200Response**](WebAppsGetHybridConnection200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListInstanceFunctionsSlot

> FunctionEnvelopeCollection webAppsListInstanceFunctionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

List the functions for a web site, or a deployment slot.

List the functions for a web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListInstanceFunctionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**FunctionEnvelopeCollection**](FunctionEnvelopeCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListInstanceIdentifiers

> WebAppInstanceCollection webAppsListInstanceIdentifiers(resourceGroupName, name, subscriptionId, apiVersion)

Gets all scale-out instances of an app.

Gets all scale-out instances of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListInstanceIdentifiers(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppInstanceCollection**](WebAppInstanceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListInstanceIdentifiersSlot

> WebAppInstanceCollection webAppsListInstanceIdentifiersSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets all scale-out instances of an app.

Gets all scale-out instances of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API gets the production slot instances.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListInstanceIdentifiersSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API gets the production slot instances. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppInstanceCollection**](WebAppInstanceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListInstanceProcessModules

> ProcessModuleInfoCollection webAppsListInstanceProcessModules(resourceGroupName, name, processId, instanceId, subscriptionId, apiVersion)

List module information for a process by its ID for a specific scaled-out instance in a web site.

List module information for a process by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListInstanceProcessModules(resourceGroupName, name, processId, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessModuleInfoCollection**](ProcessModuleInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListInstanceProcessModulesSlot

> ProcessModuleInfoCollection webAppsListInstanceProcessModulesSlot(resourceGroupName, name, processId, slot, instanceId, subscriptionId, apiVersion)

List module information for a process by its ID for a specific scaled-out instance in a web site.

List module information for a process by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListInstanceProcessModulesSlot(resourceGroupName, name, processId, slot, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessModuleInfoCollection**](ProcessModuleInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListInstanceProcessThreads

> ProcessThreadInfoCollection webAppsListInstanceProcessThreads(resourceGroupName, name, processId, instanceId, subscriptionId, apiVersion)

List the threads in a process by its ID for a specific scaled-out instance in a web site.

List the threads in a process by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListInstanceProcessThreads(resourceGroupName, name, processId, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessThreadInfoCollection**](ProcessThreadInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListInstanceProcessThreadsSlot

> ProcessThreadInfoCollection webAppsListInstanceProcessThreadsSlot(resourceGroupName, name, processId, slot, instanceId, subscriptionId, apiVersion)

List the threads in a process by its ID for a specific scaled-out instance in a web site.

List the threads in a process by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListInstanceProcessThreadsSlot(resourceGroupName, name, processId, slot, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessThreadInfoCollection**](ProcessThreadInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListInstanceProcesses

> ProcessInfoCollection webAppsListInstanceProcesses(resourceGroupName, name, instanceId, subscriptionId, apiVersion)

Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListInstanceProcesses(resourceGroupName, name, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessInfoCollection**](ProcessInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListInstanceProcessesSlot

> ProcessInfoCollection webAppsListInstanceProcessesSlot(resourceGroupName, name, slot, instanceId, subscriptionId, apiVersion)

Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let instanceId = "instanceId_example"; // String | ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \"GET api/sites/{siteName}/instances\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListInstanceProcessesSlot(resourceGroupName, name, slot, instanceId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **instanceId** | **String**| ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessInfoCollection**](ProcessInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListMetadata

> StringDictionary webAppsListMetadata(resourceGroupName, name, subscriptionId, apiVersion)

Gets the metadata of an app.

Gets the metadata of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListMetadata(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListMetadataSlot

> StringDictionary webAppsListMetadataSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the metadata of an app.

Gets the metadata of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get the metadata for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListMetadataSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get the metadata for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListMetricDefinitions

> WebAppsListMetricDefinitions200Response webAppsListMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion)

Gets all metric definitions of an app (or deployment slot, if specified).

Gets all metric definitions of an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListMetricDefinitions(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsListMetricDefinitions200Response**](WebAppsListMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListMetricDefinitionsSlot

> WebAppsListMetricDefinitions200Response webAppsListMetricDefinitionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets all metric definitions of an app (or deployment slot, if specified).

Gets all metric definitions of an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get metric definitions of the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListMetricDefinitionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get metric definitions of the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsListMetricDefinitions200Response**](WebAppsListMetricDefinitions200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListMetrics

> WebAppsListMetrics200Response webAppsListMetrics(resourceGroupName, name, subscriptionId, apiVersion, opts)

Gets performance metrics of an app (or deployment slot, if specified).

Gets performance metrics of an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'details': true, // Boolean | Specify \"true\" to include metric details in the response. It is \"false\" by default.
  'filter': "filter_example" // String | Return only metrics specified in the filter (using OData syntax). For example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.webAppsListMetrics(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **details** | **Boolean**| Specify \&quot;true\&quot; to include metric details in the response. It is \&quot;false\&quot; by default. | [optional] 
 **filter** | **String**| Return only metrics specified in the filter (using OData syntax). For example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**WebAppsListMetrics200Response**](WebAppsListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListMetricsSlot

> WebAppsListMetrics200Response webAppsListMetricsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts)

Gets performance metrics of an app (or deployment slot, if specified).

Gets performance metrics of an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get metrics of the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'details': true, // Boolean | Specify \"true\" to include metric details in the response. It is \"false\" by default.
  'filter': "filter_example" // String | Return only metrics specified in the filter (using OData syntax). For example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.webAppsListMetricsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get metrics of the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **details** | **Boolean**| Specify \&quot;true\&quot; to include metric details in the response. It is \&quot;false\&quot; by default. | [optional] 
 **filter** | **String**| Return only metrics specified in the filter (using OData syntax). For example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**WebAppsListMetrics200Response**](WebAppsListMetrics200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListNetworkFeatures

> NetworkFeatures webAppsListNetworkFeatures(resourceGroupName, name, view, subscriptionId, apiVersion)

Gets all network features used by the app (or deployment slot, if specified).

Gets all network features used by the app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let view = "view_example"; // String | The type of view. This can either be \"summary\" or \"detailed\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListNetworkFeatures(resourceGroupName, name, view, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **view** | **String**| The type of view. This can either be \&quot;summary\&quot; or \&quot;detailed\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**NetworkFeatures**](NetworkFeatures.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListNetworkFeaturesSlot

> NetworkFeatures webAppsListNetworkFeaturesSlot(resourceGroupName, name, view, slot, subscriptionId, apiVersion)

Gets all network features used by the app (or deployment slot, if specified).

Gets all network features used by the app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let view = "view_example"; // String | The type of view. This can either be \"summary\" or \"detailed\".
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get network features for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListNetworkFeaturesSlot(resourceGroupName, name, view, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **view** | **String**| The type of view. This can either be \&quot;summary\&quot; or \&quot;detailed\&quot;. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get network features for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**NetworkFeatures**](NetworkFeatures.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListPerfMonCounters

> PerfMonCounterCollection webAppsListPerfMonCounters(resourceGroupName, name, subscriptionId, apiVersion, opts)

Gets perfmon counters for web app.

Gets perfmon counters for web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.webAppsListPerfMonCounters(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**PerfMonCounterCollection**](PerfMonCounterCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListPerfMonCountersSlot

> PerfMonCounterCollection webAppsListPerfMonCountersSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts)

Gets perfmon counters for web app.

Gets perfmon counters for web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'filter': "filter_example" // String | Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter=(startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.webAppsListPerfMonCountersSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **filter** | **String**| Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**PerfMonCounterCollection**](PerfMonCounterCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListPremierAddOns

> PremierAddOn webAppsListPremierAddOns(resourceGroupName, name, subscriptionId, apiVersion)

Gets the premier add-ons of an app.

Gets the premier add-ons of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListPremierAddOns(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**PremierAddOn**](PremierAddOn.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListPremierAddOnsSlot

> PremierAddOn webAppsListPremierAddOnsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the premier add-ons of an app.

Gets the premier add-ons of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get the premier add-ons for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListPremierAddOnsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get the premier add-ons for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**PremierAddOn**](PremierAddOn.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListProcessModules

> ProcessModuleInfoCollection webAppsListProcessModules(resourceGroupName, name, processId, subscriptionId, apiVersion)

List module information for a process by its ID for a specific scaled-out instance in a web site.

List module information for a process by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListProcessModules(resourceGroupName, name, processId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessModuleInfoCollection**](ProcessModuleInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListProcessModulesSlot

> ProcessModuleInfoCollection webAppsListProcessModulesSlot(resourceGroupName, name, processId, slot, subscriptionId, apiVersion)

List module information for a process by its ID for a specific scaled-out instance in a web site.

List module information for a process by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListProcessModulesSlot(resourceGroupName, name, processId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessModuleInfoCollection**](ProcessModuleInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListProcessThreads

> ProcessThreadInfoCollection webAppsListProcessThreads(resourceGroupName, name, processId, subscriptionId, apiVersion)

List the threads in a process by its ID for a specific scaled-out instance in a web site.

List the threads in a process by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListProcessThreads(resourceGroupName, name, processId, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessThreadInfoCollection**](ProcessThreadInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListProcessThreadsSlot

> ProcessThreadInfoCollection webAppsListProcessThreadsSlot(resourceGroupName, name, processId, slot, subscriptionId, apiVersion)

List the threads in a process by its ID for a specific scaled-out instance in a web site.

List the threads in a process by its ID for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let processId = "processId_example"; // String | PID.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListProcessThreadsSlot(resourceGroupName, name, processId, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **processId** | **String**| PID. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessThreadInfoCollection**](ProcessThreadInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListProcesses

> ProcessInfoCollection webAppsListProcesses(resourceGroupName, name, subscriptionId, apiVersion)

Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListProcesses(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessInfoCollection**](ProcessInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListProcessesSlot

> ProcessInfoCollection webAppsListProcessesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListProcessesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ProcessInfoCollection**](ProcessInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListPublicCertificates

> PublicCertificateCollection webAppsListPublicCertificates(resourceGroupName, name, subscriptionId, apiVersion)

Get public certificates for an app or a deployment slot.

Get public certificates for an app or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListPublicCertificates(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**PublicCertificateCollection**](PublicCertificateCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListPublicCertificatesSlot

> PublicCertificateCollection webAppsListPublicCertificatesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Get public certificates for an app or a deployment slot.

Get public certificates for an app or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API gets hostname bindings for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListPublicCertificatesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API gets hostname bindings for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**PublicCertificateCollection**](PublicCertificateCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListPublishingCredentials

> WebAppsListPublishingCredentials200Response webAppsListPublishingCredentials(resourceGroupName, name, subscriptionId, apiVersion)

Gets the Git/FTP publishing credentials of an app.

Gets the Git/FTP publishing credentials of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListPublishingCredentials(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsListPublishingCredentials200Response**](WebAppsListPublishingCredentials200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListPublishingCredentialsSlot

> WebAppsListPublishingCredentials200Response webAppsListPublishingCredentialsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the Git/FTP publishing credentials of an app.

Gets the Git/FTP publishing credentials of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get the publishing credentials for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListPublishingCredentialsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get the publishing credentials for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsListPublishingCredentials200Response**](WebAppsListPublishingCredentials200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListPublishingProfileXmlWithSecrets

> File webAppsListPublishingProfileXmlWithSecrets(resourceGroupName, name, subscriptionId, apiVersion, publishingProfileOptions)

Gets the publishing profile for an app (or deployment slot, if specified).

Gets the publishing profile for an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let publishingProfileOptions = new WebAppsApiClient.CsmPublishingProfileOptions(); // CsmPublishingProfileOptions | Specifies publishingProfileOptions for publishing profile. For example, use {\"format\": \"FileZilla3\"} to get a FileZilla publishing profile.
apiInstance.webAppsListPublishingProfileXmlWithSecrets(resourceGroupName, name, subscriptionId, apiVersion, publishingProfileOptions, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **publishingProfileOptions** | [**CsmPublishingProfileOptions**](CsmPublishingProfileOptions.md)| Specifies publishingProfileOptions for publishing profile. For example, use {\&quot;format\&quot;: \&quot;FileZilla3\&quot;} to get a FileZilla publishing profile. | 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/xml


## webAppsListPublishingProfileXmlWithSecretsSlot

> File webAppsListPublishingProfileXmlWithSecretsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, publishingProfileOptions)

Gets the publishing profile for an app (or deployment slot, if specified).

Gets the publishing profile for an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get the publishing profile for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let publishingProfileOptions = new WebAppsApiClient.CsmPublishingProfileOptions(); // CsmPublishingProfileOptions | Specifies publishingProfileOptions for publishing profile. For example, use {\"format\": \"FileZilla3\"} to get a FileZilla publishing profile.
apiInstance.webAppsListPublishingProfileXmlWithSecretsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, publishingProfileOptions, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get the publishing profile for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **publishingProfileOptions** | [**CsmPublishingProfileOptions**](CsmPublishingProfileOptions.md)| Specifies publishingProfileOptions for publishing profile. For example, use {\&quot;format\&quot;: \&quot;FileZilla3\&quot;} to get a FileZilla publishing profile. | 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/xml


## webAppsListRelayServiceConnections

> RelayServiceConnectionEntity webAppsListRelayServiceConnections(resourceGroupName, name, subscriptionId, apiVersion)

Gets hybrid connections configured for an app (or deployment slot, if specified).

Gets hybrid connections configured for an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListRelayServiceConnections(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListRelayServiceConnectionsSlot

> RelayServiceConnectionEntity webAppsListRelayServiceConnectionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets hybrid connections configured for an app (or deployment slot, if specified).

Gets hybrid connections configured for an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get hybrid connections for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListRelayServiceConnectionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get hybrid connections for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListSiteExtensions

> SiteExtensionInfoCollection webAppsListSiteExtensions(resourceGroupName, name, subscriptionId, apiVersion)

Get list of siteextensions for a web site, or a deployment slot.

Get list of siteextensions for a web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListSiteExtensions(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteExtensionInfoCollection**](SiteExtensionInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListSiteExtensionsSlot

> SiteExtensionInfoCollection webAppsListSiteExtensionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Get list of siteextensions for a web site, or a deployment slot.

Get list of siteextensions for a web site, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListSiteExtensionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SiteExtensionInfoCollection**](SiteExtensionInfoCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListSitePushSettings

> WebAppsUpdateSitePushSettingsRequest webAppsListSitePushSettings(resourceGroupName, name, subscriptionId, apiVersion)

Gets the Push settings associated with web app.

Gets the Push settings associated with web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListSitePushSettings(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsUpdateSitePushSettingsRequest**](WebAppsUpdateSitePushSettingsRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListSitePushSettingsSlot

> WebAppsUpdateSitePushSettingsRequest webAppsListSitePushSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the Push settings associated with web app.

Gets the Push settings associated with web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListSitePushSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsUpdateSitePushSettingsRequest**](WebAppsUpdateSitePushSettingsRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListSlotConfigurationNames

> SlotConfigNamesResource webAppsListSlotConfigurationNames(resourceGroupName, name, subscriptionId, apiVersion)

Gets the names of app settings and connection strings that stick to the slot (not swapped).

Gets the names of app settings and connection strings that stick to the slot (not swapped).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListSlotConfigurationNames(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SlotConfigNamesResource**](SlotConfigNamesResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListSlotDifferencesFromProduction

> SlotDifferenceCollection webAppsListSlotDifferencesFromProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity)

Get the difference in configuration settings between two web app slots.

Get the difference in configuration settings between two web app slots.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let slotSwapEntity = new WebAppsApiClient.CsmSlotEntity(); // CsmSlotEntity | JSON object that contains the target slot name. See example.
apiInstance.webAppsListSlotDifferencesFromProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| JSON object that contains the target slot name. See example. | 

### Return type

[**SlotDifferenceCollection**](SlotDifferenceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsListSlotDifferencesSlot

> SlotDifferenceCollection webAppsListSlotDifferencesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity)

Get the difference in configuration settings between two web app slots.

Get the difference in configuration settings between two web app slots.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the source slot. If a slot is not specified, the production slot is used as the source slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let slotSwapEntity = new WebAppsApiClient.CsmSlotEntity(); // CsmSlotEntity | JSON object that contains the target slot name. See example.
apiInstance.webAppsListSlotDifferencesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the source slot. If a slot is not specified, the production slot is used as the source slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| JSON object that contains the target slot name. See example. | 

### Return type

[**SlotDifferenceCollection**](SlotDifferenceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsListSlots

> WebAppsList200Response webAppsListSlots(resourceGroupName, name, subscriptionId, apiVersion)

Gets an app&#39;s deployment slots.

Gets an app&#39;s deployment slots.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListSlots(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebAppsList200Response**](WebAppsList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListSnapshots

> SnapshotCollection webAppsListSnapshots(resourceGroupName, name, subscriptionId, apiVersion)

Returns all Snapshots to the user.

Returns all Snapshots to the user.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Website Name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListSnapshots(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Website Name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SnapshotCollection**](SnapshotCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListSnapshotsFromDRSecondary

> SnapshotCollection webAppsListSnapshotsFromDRSecondary(resourceGroupName, name, subscriptionId, apiVersion)

Returns all Snapshots to the user from DRSecondary endpoint.

Returns all Snapshots to the user from DRSecondary endpoint.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Website Name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListSnapshotsFromDRSecondary(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Website Name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SnapshotCollection**](SnapshotCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListSnapshotsFromDRSecondarySlot

> SnapshotCollection webAppsListSnapshotsFromDRSecondarySlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Returns all Snapshots to the user from DRSecondary endpoint.

Returns all Snapshots to the user from DRSecondary endpoint.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Website Name.
let slot = "slot_example"; // String | Website Slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListSnapshotsFromDRSecondarySlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Website Name. | 
 **slot** | **String**| Website Slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SnapshotCollection**](SnapshotCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListSnapshotsSlot

> SnapshotCollection webAppsListSnapshotsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Returns all Snapshots to the user.

Returns all Snapshots to the user.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Website Name.
let slot = "slot_example"; // String | Website Slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListSnapshotsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Website Name. | 
 **slot** | **String**| Website Slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**SnapshotCollection**](SnapshotCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListSyncFunctionTriggers

> FunctionSecrets webAppsListSyncFunctionTriggers(resourceGroupName, name, subscriptionId, apiVersion)

This is to allow calling via powershell and ARM template.

This is to allow calling via powershell and ARM template.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListSyncFunctionTriggers(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**FunctionSecrets**](FunctionSecrets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListSyncFunctionTriggersSlot

> FunctionSecrets webAppsListSyncFunctionTriggersSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

This is to allow calling via powershell and ARM template.

This is to allow calling via powershell and ARM template.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListSyncFunctionTriggersSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**FunctionSecrets**](FunctionSecrets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListSyncStatus

> webAppsListSyncStatus(resourceGroupName, name, subscriptionId, apiVersion)

This is to allow calling via powershell and ARM template.

This is to allow calling via powershell and ARM template.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListSyncStatus(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListSyncStatusSlot

> webAppsListSyncStatusSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

This is to allow calling via powershell and ARM template.

This is to allow calling via powershell and ARM template.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListSyncStatusSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListTriggeredWebJobHistory

> TriggeredJobHistoryCollection webAppsListTriggeredWebJobHistory(resourceGroupName, name, webJobName, subscriptionId, apiVersion)

List a triggered web job&#39;s history for an app, or a deployment slot.

List a triggered web job&#39;s history for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListTriggeredWebJobHistory(resourceGroupName, name, webJobName, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**TriggeredJobHistoryCollection**](TriggeredJobHistoryCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListTriggeredWebJobHistorySlot

> TriggeredJobHistoryCollection webAppsListTriggeredWebJobHistorySlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion)

List a triggered web job&#39;s history for an app, or a deployment slot.

List a triggered web job&#39;s history for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListTriggeredWebJobHistorySlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**TriggeredJobHistoryCollection**](TriggeredJobHistoryCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListTriggeredWebJobs

> TriggeredWebJobCollection webAppsListTriggeredWebJobs(resourceGroupName, name, subscriptionId, apiVersion)

List triggered web jobs for an app, or a deployment slot.

List triggered web jobs for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListTriggeredWebJobs(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**TriggeredWebJobCollection**](TriggeredWebJobCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListTriggeredWebJobsSlot

> TriggeredWebJobCollection webAppsListTriggeredWebJobsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

List triggered web jobs for an app, or a deployment slot.

List triggered web jobs for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListTriggeredWebJobsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**TriggeredWebJobCollection**](TriggeredWebJobCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListUsages

> WebAppsListUsagesSlot200Response webAppsListUsages(resourceGroupName, name, subscriptionId, apiVersion, opts)

Gets the quota usage information of an app (or deployment slot, if specified).

Gets the quota usage information of an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'filter': "filter_example" // String | Return only information specified in the filter (using OData syntax). For example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.webAppsListUsages(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **filter** | **String**| Return only information specified in the filter (using OData syntax). For example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**WebAppsListUsagesSlot200Response**](WebAppsListUsagesSlot200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListUsagesSlot

> WebAppsListUsagesSlot200Response webAppsListUsagesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts)

Gets the quota usage information of an app (or deployment slot, if specified).

Gets the quota usage information of an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get quota information of the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'filter': "filter_example" // String | Return only information specified in the filter (using OData syntax). For example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[Hour|Minute|Day]'.
};
apiInstance.webAppsListUsagesSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get quota information of the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **filter** | **String**| Return only information specified in the filter (using OData syntax). For example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;. | [optional] 

### Return type

[**WebAppsListUsagesSlot200Response**](WebAppsListUsagesSlot200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListVnetConnections

> [WebAppsListVnetConnectionsSlot200ResponseInner] webAppsListVnetConnections(resourceGroupName, name, subscriptionId, apiVersion)

Gets the virtual networks the app (or deployment slot) is connected to.

Gets the virtual networks the app (or deployment slot) is connected to.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListVnetConnections(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[WebAppsListVnetConnectionsSlot200ResponseInner]**](WebAppsListVnetConnectionsSlot200ResponseInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListVnetConnectionsSlot

> [WebAppsListVnetConnectionsSlot200ResponseInner] webAppsListVnetConnectionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Gets the virtual networks the app (or deployment slot) is connected to.

Gets the virtual networks the app (or deployment slot) is connected to.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will get virtual network connections for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListVnetConnectionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will get virtual network connections for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**[WebAppsListVnetConnectionsSlot200ResponseInner]**](WebAppsListVnetConnectionsSlot200ResponseInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListWebJobs

> WebJobCollection webAppsListWebJobs(resourceGroupName, name, subscriptionId, apiVersion)

List webjobs for an app, or a deployment slot.

List webjobs for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListWebJobs(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebJobCollection**](WebJobCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsListWebJobsSlot

> WebJobCollection webAppsListWebJobsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

List webjobs for an app, or a deployment slot.

List webjobs for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsListWebJobsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**WebJobCollection**](WebJobCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsMigrateMySql

> WebAppsMigrateMySql200Response webAppsMigrateMySql(resourceGroupName, name, subscriptionId, apiVersion, migrationRequestEnvelope)

Migrates a local (in-app) MySql database to a remote MySql database.

Migrates a local (in-app) MySql database to a remote MySql database.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let migrationRequestEnvelope = new WebAppsApiClient.MigrateMySqlRequest(); // MigrateMySqlRequest | MySql migration options.
apiInstance.webAppsMigrateMySql(resourceGroupName, name, subscriptionId, apiVersion, migrationRequestEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **migrationRequestEnvelope** | [**MigrateMySqlRequest**](MigrateMySqlRequest.md)| MySql migration options. | 

### Return type

[**WebAppsMigrateMySql200Response**](WebAppsMigrateMySql200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsMigrateStorage

> StorageMigrationResponse webAppsMigrateStorage(subscriptionName, resourceGroupName, name, subscriptionId, apiVersion, migrationOptions)

Restores a web app.

Restores a web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let subscriptionName = "subscriptionName_example"; // String | Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let migrationOptions = new WebAppsApiClient.StorageMigrationOptions(); // StorageMigrationOptions | Migration migrationOptions.
apiInstance.webAppsMigrateStorage(subscriptionName, resourceGroupName, name, subscriptionId, apiVersion, migrationOptions, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionName** | **String**| Azure subscription. | 
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **migrationOptions** | [**StorageMigrationOptions**](StorageMigrationOptions.md)| Migration migrationOptions. | 

### Return type

[**StorageMigrationResponse**](StorageMigrationResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsPutPrivateAccessVnet

> PrivateAccess webAppsPutPrivateAccessVnet(resourceGroupName, name, subscriptionId, apiVersion, access)

Sets data around private site access enablement and authorized Virtual Networks that can access the site.

Sets data around private site access enablement and authorized Virtual Networks that can access the site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let access = new WebAppsApiClient.PrivateAccess(); // PrivateAccess | The information for the private access
apiInstance.webAppsPutPrivateAccessVnet(resourceGroupName, name, subscriptionId, apiVersion, access, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **access** | [**PrivateAccess**](PrivateAccess.md)| The information for the private access | 

### Return type

[**PrivateAccess**](PrivateAccess.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsPutPrivateAccessVnetSlot

> PrivateAccess webAppsPutPrivateAccessVnetSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, access)

Sets data around private site access enablement and authorized Virtual Networks that can access the site.

Sets data around private site access enablement and authorized Virtual Networks that can access the site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let slot = "slot_example"; // String | The name of the slot for the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let access = new WebAppsApiClient.PrivateAccess(); // PrivateAccess | The information for the private access
apiInstance.webAppsPutPrivateAccessVnetSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, access, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **slot** | **String**| The name of the slot for the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **access** | [**PrivateAccess**](PrivateAccess.md)| The information for the private access | 

### Return type

[**PrivateAccess**](PrivateAccess.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsRecoverSiteConfigurationSnapshot

> webAppsRecoverSiteConfigurationSnapshot(resourceGroupName, name, snapshotId, subscriptionId, apiVersion)

Reverts the configuration of an app to a previous snapshot.

Reverts the configuration of an app to a previous snapshot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let snapshotId = "snapshotId_example"; // String | The ID of the snapshot to read.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsRecoverSiteConfigurationSnapshot(resourceGroupName, name, snapshotId, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **snapshotId** | **String**| The ID of the snapshot to read. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsRecoverSiteConfigurationSnapshotSlot

> webAppsRecoverSiteConfigurationSnapshotSlot(resourceGroupName, name, snapshotId, slot, subscriptionId, apiVersion)

Reverts the configuration of an app to a previous snapshot.

Reverts the configuration of an app to a previous snapshot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let snapshotId = "snapshotId_example"; // String | The ID of the snapshot to read.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsRecoverSiteConfigurationSnapshotSlot(resourceGroupName, name, snapshotId, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **snapshotId** | **String**| The ID of the snapshot to read. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsResetProductionSlotConfig

> webAppsResetProductionSlotConfig(resourceGroupName, name, subscriptionId, apiVersion)

Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.

Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsResetProductionSlotConfig(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsResetSlotConfigurationSlot

> webAppsResetSlotConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.

Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API resets configuration settings for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsResetSlotConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API resets configuration settings for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsRestart

> webAppsRestart(resourceGroupName, name, subscriptionId, apiVersion, opts)

Restarts an app (or deployment slot, if specified).

Restarts an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'softRestart': true, // Boolean | Specify true to apply the configuration settings and restarts the app only if necessary. By default, the API always restarts and reprovisions the app.
  'synchronous': true // Boolean | Specify true to block until the app is restarted. By default, it is set to false, and the API responds immediately (asynchronous).
};
apiInstance.webAppsRestart(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **softRestart** | **Boolean**| Specify true to apply the configuration settings and restarts the app only if necessary. By default, the API always restarts and reprovisions the app. | [optional] 
 **synchronous** | **Boolean**| Specify true to block until the app is restarted. By default, it is set to false, and the API responds immediately (asynchronous). | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsRestartSlot

> webAppsRestartSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts)

Restarts an app (or deployment slot, if specified).

Restarts an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will restart the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'softRestart': true, // Boolean | Specify true to apply the configuration settings and restarts the app only if necessary. By default, the API always restarts and reprovisions the app.
  'synchronous': true // Boolean | Specify true to block until the app is restarted. By default, it is set to false, and the API responds immediately (asynchronous).
};
apiInstance.webAppsRestartSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will restart the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **softRestart** | **Boolean**| Specify true to apply the configuration settings and restarts the app only if necessary. By default, the API always restarts and reprovisions the app. | [optional] 
 **synchronous** | **Boolean**| Specify true to block until the app is restarted. By default, it is set to false, and the API responds immediately (asynchronous). | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsRestore

> webAppsRestore(resourceGroupName, name, backupId, subscriptionId, apiVersion, request)

Restores a specific backup to another app (or deployment slot, if specified).

Restores a specific backup to another app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let backupId = "backupId_example"; // String | ID of the backup.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebAppsApiClient.RestoreRequest(); // RestoreRequest | Information on restore request .
apiInstance.webAppsRestore(resourceGroupName, name, backupId, subscriptionId, apiVersion, request, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **backupId** | **String**| ID of the backup. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **request** | [**RestoreRequest**](RestoreRequest.md)| Information on restore request . | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## webAppsRestoreFromBackupBlob

> webAppsRestoreFromBackupBlob(resourceGroupName, name, subscriptionId, apiVersion, request)

Restores an app from a backup blob in Azure Storage.

Restores an app from a backup blob in Azure Storage.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebAppsApiClient.RestoreRequest(); // RestoreRequest | Information on restore request .
apiInstance.webAppsRestoreFromBackupBlob(resourceGroupName, name, subscriptionId, apiVersion, request, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **request** | [**RestoreRequest**](RestoreRequest.md)| Information on restore request . | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## webAppsRestoreFromBackupBlobSlot

> webAppsRestoreFromBackupBlobSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request)

Restores an app from a backup blob in Azure Storage.

Restores an app from a backup blob in Azure Storage.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will restore a backup of the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebAppsApiClient.RestoreRequest(); // RestoreRequest | Information on restore request .
apiInstance.webAppsRestoreFromBackupBlobSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will restore a backup of the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **request** | [**RestoreRequest**](RestoreRequest.md)| Information on restore request . | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## webAppsRestoreFromDeletedApp

> webAppsRestoreFromDeletedApp(resourceGroupName, name, subscriptionId, apiVersion, restoreRequest)

Restores a deleted web app to this web app.

Restores a deleted web app to this web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let restoreRequest = new WebAppsApiClient.DeletedAppRestoreRequest(); // DeletedAppRestoreRequest | Deleted web app restore information.
apiInstance.webAppsRestoreFromDeletedApp(resourceGroupName, name, subscriptionId, apiVersion, restoreRequest, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **restoreRequest** | [**DeletedAppRestoreRequest**](DeletedAppRestoreRequest.md)| Deleted web app restore information. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## webAppsRestoreFromDeletedAppSlot

> webAppsRestoreFromDeletedAppSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, restoreRequest)

Restores a deleted web app to this web app.

Restores a deleted web app to this web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let restoreRequest = new WebAppsApiClient.DeletedAppRestoreRequest(); // DeletedAppRestoreRequest | Deleted web app restore information.
apiInstance.webAppsRestoreFromDeletedAppSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, restoreRequest, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **restoreRequest** | [**DeletedAppRestoreRequest**](DeletedAppRestoreRequest.md)| Deleted web app restore information. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## webAppsRestoreSlot

> webAppsRestoreSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, request)

Restores a specific backup to another app (or deployment slot, if specified).

Restores a specific backup to another app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let backupId = "backupId_example"; // String | ID of the backup.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will restore a backup of the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebAppsApiClient.RestoreRequest(); // RestoreRequest | Information on restore request .
apiInstance.webAppsRestoreSlot(resourceGroupName, name, backupId, slot, subscriptionId, apiVersion, request, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **backupId** | **String**| ID of the backup. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will restore a backup of the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **request** | [**RestoreRequest**](RestoreRequest.md)| Information on restore request . | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## webAppsRestoreSnapshot

> webAppsRestoreSnapshot(resourceGroupName, name, subscriptionId, apiVersion, restoreRequest)

Restores a web app from a snapshot.

Restores a web app from a snapshot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let restoreRequest = new WebAppsApiClient.SnapshotRestoreRequest(); // SnapshotRestoreRequest | Snapshot restore settings. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API.
apiInstance.webAppsRestoreSnapshot(resourceGroupName, name, subscriptionId, apiVersion, restoreRequest, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **restoreRequest** | [**SnapshotRestoreRequest**](SnapshotRestoreRequest.md)| Snapshot restore settings. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## webAppsRestoreSnapshotSlot

> webAppsRestoreSnapshotSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, restoreRequest)

Restores a web app from a snapshot.

Restores a web app from a snapshot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let restoreRequest = new WebAppsApiClient.SnapshotRestoreRequest(); // SnapshotRestoreRequest | Snapshot restore settings. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API.
apiInstance.webAppsRestoreSnapshotSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, restoreRequest, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **restoreRequest** | [**SnapshotRestoreRequest**](SnapshotRestoreRequest.md)| Snapshot restore settings. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## webAppsRunTriggeredWebJob

> webAppsRunTriggeredWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion)

Run a triggered web job for an app, or a deployment slot.

Run a triggered web job for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsRunTriggeredWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsRunTriggeredWebJobSlot

> webAppsRunTriggeredWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion)

Run a triggered web job for an app, or a deployment slot.

Run a triggered web job for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsRunTriggeredWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsStart

> webAppsStart(resourceGroupName, name, subscriptionId, apiVersion)

Starts an app (or deployment slot, if specified).

Starts an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsStart(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsStartContinuousWebJob

> webAppsStartContinuousWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion)

Start a continuous web job for an app, or a deployment slot.

Start a continuous web job for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsStartContinuousWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsStartContinuousWebJobSlot

> webAppsStartContinuousWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion)

Start a continuous web job for an app, or a deployment slot.

Start a continuous web job for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsStartContinuousWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsStartNetworkTrace

> [NetworkTrace] webAppsStartNetworkTrace(resourceGroupName, name, subscriptionId, apiVersion, opts)

Start capturing network packets for the site.

Start capturing network packets for the site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'durationInSeconds': 56, // Number | The duration to keep capturing in seconds.
  'maxFrameLength': 56, // Number | The maximum frame length in bytes (Optional).
  'sasUrl': "sasUrl_example" // String | The Blob URL to store capture file.
};
apiInstance.webAppsStartNetworkTrace(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **durationInSeconds** | **Number**| The duration to keep capturing in seconds. | [optional] 
 **maxFrameLength** | **Number**| The maximum frame length in bytes (Optional). | [optional] 
 **sasUrl** | **String**| The Blob URL to store capture file. | [optional] 

### Return type

[**[NetworkTrace]**](NetworkTrace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsStartNetworkTraceSlot

> [NetworkTrace] webAppsStartNetworkTraceSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts)

Start capturing network packets for the site.

Start capturing network packets for the site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let slot = "slot_example"; // String | The name of the slot for this web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'durationInSeconds': 56, // Number | The duration to keep capturing in seconds.
  'maxFrameLength': 56, // Number | The maximum frame length in bytes (Optional).
  'sasUrl': "sasUrl_example" // String | The Blob URL to store capture file.
};
apiInstance.webAppsStartNetworkTraceSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **slot** | **String**| The name of the slot for this web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **durationInSeconds** | **Number**| The duration to keep capturing in seconds. | [optional] 
 **maxFrameLength** | **Number**| The maximum frame length in bytes (Optional). | [optional] 
 **sasUrl** | **String**| The Blob URL to store capture file. | [optional] 

### Return type

[**[NetworkTrace]**](NetworkTrace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsStartSlot

> webAppsStartSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Starts an app (or deployment slot, if specified).

Starts an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will start the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsStartSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will start the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsStartWebSiteNetworkTrace

> String webAppsStartWebSiteNetworkTrace(resourceGroupName, name, subscriptionId, apiVersion, opts)

Start capturing network packets for the site (To be deprecated).

Start capturing network packets for the site (To be deprecated).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'durationInSeconds': 56, // Number | The duration to keep capturing in seconds.
  'maxFrameLength': 56, // Number | The maximum frame length in bytes (Optional).
  'sasUrl': "sasUrl_example" // String | The Blob URL to store capture file.
};
apiInstance.webAppsStartWebSiteNetworkTrace(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **durationInSeconds** | **Number**| The duration to keep capturing in seconds. | [optional] 
 **maxFrameLength** | **Number**| The maximum frame length in bytes (Optional). | [optional] 
 **sasUrl** | **String**| The Blob URL to store capture file. | [optional] 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsStartWebSiteNetworkTraceOperation

> [NetworkTrace] webAppsStartWebSiteNetworkTraceOperation(resourceGroupName, name, subscriptionId, apiVersion, opts)

Start capturing network packets for the site.

Start capturing network packets for the site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'durationInSeconds': 56, // Number | The duration to keep capturing in seconds.
  'maxFrameLength': 56, // Number | The maximum frame length in bytes (Optional).
  'sasUrl': "sasUrl_example" // String | The Blob URL to store capture file.
};
apiInstance.webAppsStartWebSiteNetworkTraceOperation(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **durationInSeconds** | **Number**| The duration to keep capturing in seconds. | [optional] 
 **maxFrameLength** | **Number**| The maximum frame length in bytes (Optional). | [optional] 
 **sasUrl** | **String**| The Blob URL to store capture file. | [optional] 

### Return type

[**[NetworkTrace]**](NetworkTrace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsStartWebSiteNetworkTraceOperationSlot

> [NetworkTrace] webAppsStartWebSiteNetworkTraceOperationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts)

Start capturing network packets for the site.

Start capturing network packets for the site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let slot = "slot_example"; // String | The name of the slot for this web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'durationInSeconds': 56, // Number | The duration to keep capturing in seconds.
  'maxFrameLength': 56, // Number | The maximum frame length in bytes (Optional).
  'sasUrl': "sasUrl_example" // String | The Blob URL to store capture file.
};
apiInstance.webAppsStartWebSiteNetworkTraceOperationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **slot** | **String**| The name of the slot for this web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **durationInSeconds** | **Number**| The duration to keep capturing in seconds. | [optional] 
 **maxFrameLength** | **Number**| The maximum frame length in bytes (Optional). | [optional] 
 **sasUrl** | **String**| The Blob URL to store capture file. | [optional] 

### Return type

[**[NetworkTrace]**](NetworkTrace.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsStartWebSiteNetworkTraceSlot

> String webAppsStartWebSiteNetworkTraceSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts)

Start capturing network packets for the site (To be deprecated).

Start capturing network packets for the site (To be deprecated).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let slot = "slot_example"; // String | The name of the slot for this web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'durationInSeconds': 56, // Number | The duration to keep capturing in seconds.
  'maxFrameLength': 56, // Number | The maximum frame length in bytes (Optional).
  'sasUrl': "sasUrl_example" // String | The Blob URL to store capture file.
};
apiInstance.webAppsStartWebSiteNetworkTraceSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **slot** | **String**| The name of the slot for this web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **durationInSeconds** | **Number**| The duration to keep capturing in seconds. | [optional] 
 **maxFrameLength** | **Number**| The maximum frame length in bytes (Optional). | [optional] 
 **sasUrl** | **String**| The Blob URL to store capture file. | [optional] 

### Return type

**String**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsStop

> webAppsStop(resourceGroupName, name, subscriptionId, apiVersion)

Stops an app (or deployment slot, if specified).

Stops an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsStop(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsStopContinuousWebJob

> webAppsStopContinuousWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion)

Stop a continuous web job for an app, or a deployment slot.

Stop a continuous web job for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsStopContinuousWebJob(resourceGroupName, name, webJobName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsStopContinuousWebJobSlot

> webAppsStopContinuousWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion)

Stop a continuous web job for an app, or a deployment slot.

Stop a continuous web job for an app, or a deployment slot.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site name.
let webJobName = "webJobName_example"; // String | Name of Web Job.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsStopContinuousWebJobSlot(resourceGroupName, name, webJobName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site name. | 
 **webJobName** | **String**| Name of Web Job. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsStopNetworkTrace

> webAppsStopNetworkTrace(resourceGroupName, name, subscriptionId, apiVersion)

Stop ongoing capturing network packets for the site.

Stop ongoing capturing network packets for the site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsStopNetworkTrace(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsStopNetworkTraceSlot

> webAppsStopNetworkTraceSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Stop ongoing capturing network packets for the site.

Stop ongoing capturing network packets for the site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let slot = "slot_example"; // String | The name of the slot for this web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsStopNetworkTraceSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **slot** | **String**| The name of the slot for this web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsStopSlot

> webAppsStopSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Stops an app (or deployment slot, if specified).

Stops an app (or deployment slot, if specified).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will stop the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsStopSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will stop the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsStopWebSiteNetworkTrace

> webAppsStopWebSiteNetworkTrace(resourceGroupName, name, subscriptionId, apiVersion)

Stop ongoing capturing network packets for the site.

Stop ongoing capturing network packets for the site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsStopWebSiteNetworkTrace(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsStopWebSiteNetworkTraceSlot

> webAppsStopWebSiteNetworkTraceSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Stop ongoing capturing network packets for the site.

Stop ongoing capturing network packets for the site.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let slot = "slot_example"; // String | The name of the slot for this web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsStopWebSiteNetworkTraceSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **slot** | **String**| The name of the slot for this web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsSwapSlotSlot

> webAppsSwapSlotSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity)

Swaps two deployment slots of an app.

Swaps two deployment slots of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the source slot. If a slot is not specified, the production slot is used as the source slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let slotSwapEntity = new WebAppsApiClient.CsmSlotEntity(); // CsmSlotEntity | JSON object that contains the target slot name. See example.
apiInstance.webAppsSwapSlotSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, slotSwapEntity, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the source slot. If a slot is not specified, the production slot is used as the source slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| JSON object that contains the target slot name. See example. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## webAppsSwapSlotWithProduction

> webAppsSwapSlotWithProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity)

Swaps two deployment slots of an app.

Swaps two deployment slots of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let slotSwapEntity = new WebAppsApiClient.CsmSlotEntity(); // CsmSlotEntity | JSON object that contains the target slot name. See example.
apiInstance.webAppsSwapSlotWithProduction(resourceGroupName, name, subscriptionId, apiVersion, slotSwapEntity, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **slotSwapEntity** | [**CsmSlotEntity**](CsmSlotEntity.md)| JSON object that contains the target slot name. See example. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## webAppsSyncFunctionTriggers

> webAppsSyncFunctionTriggers(resourceGroupName, name, subscriptionId, apiVersion)

Syncs function trigger metadata to the management database

Syncs function trigger metadata to the management database

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsSyncFunctionTriggers(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsSyncFunctionTriggersSlot

> webAppsSyncFunctionTriggersSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Syncs function trigger metadata to the management database

Syncs function trigger metadata to the management database

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsSyncFunctionTriggersSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsSyncFunctions

> webAppsSyncFunctions(resourceGroupName, name, subscriptionId, apiVersion)

Syncs function trigger metadata to the management database

Syncs function trigger metadata to the management database

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsSyncFunctions(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsSyncFunctionsSlot

> webAppsSyncFunctionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Syncs function trigger metadata to the management database

Syncs function trigger metadata to the management database

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsSyncFunctionsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webAppsSyncRepository

> webAppsSyncRepository(resourceGroupName, name, subscriptionId, apiVersion)

Sync web app repository.

Sync web app repository.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsSyncRepository(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsSyncRepositorySlot

> webAppsSyncRepositorySlot(resourceGroupName, name, slot, subscriptionId, apiVersion)

Sync web app repository.

Sync web app repository.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.webAppsSyncRepositorySlot(resourceGroupName, name, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webAppsUpdate

> WebAppsGet200Response webAppsUpdate(resourceGroupName, name, subscriptionId, apiVersion, siteEnvelope)

Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Unique name of the app to create or update. To create or update a deployment slot, use the {slot} parameter.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteEnvelope = new WebAppsApiClient.SitePatchResource(); // SitePatchResource | A JSON representation of the app properties. See example.
apiInstance.webAppsUpdate(resourceGroupName, name, subscriptionId, apiVersion, siteEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Unique name of the app to create or update. To create or update a deployment slot, use the {slot} parameter. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteEnvelope** | [**SitePatchResource**](SitePatchResource.md)| A JSON representation of the app properties. See example. | 

### Return type

[**WebAppsGet200Response**](WebAppsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateApplicationSettings

> StringDictionary webAppsUpdateApplicationSettings(resourceGroupName, name, subscriptionId, apiVersion, appSettings)

Replaces the application settings of an app.

Replaces the application settings of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let appSettings = new WebAppsApiClient.StringDictionary(); // StringDictionary | Application settings of the app.
apiInstance.webAppsUpdateApplicationSettings(resourceGroupName, name, subscriptionId, apiVersion, appSettings, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **appSettings** | [**StringDictionary**](StringDictionary.md)| Application settings of the app. | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateApplicationSettingsSlot

> StringDictionary webAppsUpdateApplicationSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, appSettings)

Replaces the application settings of an app.

Replaces the application settings of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will update the application settings for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let appSettings = new WebAppsApiClient.StringDictionary(); // StringDictionary | Application settings of the app.
apiInstance.webAppsUpdateApplicationSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, appSettings, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will update the application settings for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **appSettings** | [**StringDictionary**](StringDictionary.md)| Application settings of the app. | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateAuthSettings

> SiteAuthSettings webAppsUpdateAuthSettings(resourceGroupName, name, subscriptionId, apiVersion, siteAuthSettings)

Updates the Authentication / Authorization settings associated with web app.

Updates the Authentication / Authorization settings associated with web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteAuthSettings = new WebAppsApiClient.SiteAuthSettings(); // SiteAuthSettings | Auth settings associated with web app.
apiInstance.webAppsUpdateAuthSettings(resourceGroupName, name, subscriptionId, apiVersion, siteAuthSettings, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteAuthSettings** | [**SiteAuthSettings**](SiteAuthSettings.md)| Auth settings associated with web app. | 

### Return type

[**SiteAuthSettings**](SiteAuthSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateAuthSettingsSlot

> SiteAuthSettings webAppsUpdateAuthSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteAuthSettings)

Updates the Authentication / Authorization settings associated with web app.

Updates the Authentication / Authorization settings associated with web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteAuthSettings = new WebAppsApiClient.SiteAuthSettings(); // SiteAuthSettings | Auth settings associated with web app.
apiInstance.webAppsUpdateAuthSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteAuthSettings, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteAuthSettings** | [**SiteAuthSettings**](SiteAuthSettings.md)| Auth settings associated with web app. | 

### Return type

[**SiteAuthSettings**](SiteAuthSettings.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateAzureStorageAccounts

> AzureStoragePropertyDictionaryResource webAppsUpdateAzureStorageAccounts(resourceGroupName, name, subscriptionId, apiVersion, azureStorageAccounts)

Updates the Azure storage account configurations of an app.

Updates the Azure storage account configurations of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let azureStorageAccounts = new WebAppsApiClient.AzureStoragePropertyDictionaryResource(); // AzureStoragePropertyDictionaryResource | Azure storage accounts of the app.
apiInstance.webAppsUpdateAzureStorageAccounts(resourceGroupName, name, subscriptionId, apiVersion, azureStorageAccounts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **azureStorageAccounts** | [**AzureStoragePropertyDictionaryResource**](AzureStoragePropertyDictionaryResource.md)| Azure storage accounts of the app. | 

### Return type

[**AzureStoragePropertyDictionaryResource**](AzureStoragePropertyDictionaryResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateAzureStorageAccountsSlot

> AzureStoragePropertyDictionaryResource webAppsUpdateAzureStorageAccountsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, azureStorageAccounts)

Updates the Azure storage account configurations of an app.

Updates the Azure storage account configurations of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will update the Azure storage account configurations for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let azureStorageAccounts = new WebAppsApiClient.AzureStoragePropertyDictionaryResource(); // AzureStoragePropertyDictionaryResource | Azure storage accounts of the app.
apiInstance.webAppsUpdateAzureStorageAccountsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, azureStorageAccounts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will update the Azure storage account configurations for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **azureStorageAccounts** | [**AzureStoragePropertyDictionaryResource**](AzureStoragePropertyDictionaryResource.md)| Azure storage accounts of the app. | 

### Return type

[**AzureStoragePropertyDictionaryResource**](AzureStoragePropertyDictionaryResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateBackupConfiguration

> BackupRequest webAppsUpdateBackupConfiguration(resourceGroupName, name, subscriptionId, apiVersion, request)

Updates the backup configuration of an app.

Updates the backup configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebAppsApiClient.BackupRequest(); // BackupRequest | Edited backup configuration.
apiInstance.webAppsUpdateBackupConfiguration(resourceGroupName, name, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **request** | [**BackupRequest**](BackupRequest.md)| Edited backup configuration. | 

### Return type

[**BackupRequest**](BackupRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateBackupConfigurationSlot

> BackupRequest webAppsUpdateBackupConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request)

Updates the backup configuration of an app.

Updates the backup configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will update the backup configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let request = new WebAppsApiClient.BackupRequest(); // BackupRequest | Edited backup configuration.
apiInstance.webAppsUpdateBackupConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, request, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will update the backup configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **request** | [**BackupRequest**](BackupRequest.md)| Edited backup configuration. | 

### Return type

[**BackupRequest**](BackupRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateConfiguration

> SiteConfigResource webAppsUpdateConfiguration(resourceGroupName, name, subscriptionId, apiVersion, siteConfig)

Updates the configuration of an app.

Updates the configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteConfig = new WebAppsApiClient.SiteConfigResource(); // SiteConfigResource | JSON representation of a SiteConfig object. See example.
apiInstance.webAppsUpdateConfiguration(resourceGroupName, name, subscriptionId, apiVersion, siteConfig, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteConfig** | [**SiteConfigResource**](SiteConfigResource.md)| JSON representation of a SiteConfig object. See example. | 

### Return type

[**SiteConfigResource**](SiteConfigResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateConfigurationSlot

> SiteConfigResource webAppsUpdateConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteConfig)

Updates the configuration of an app.

Updates the configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will update configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteConfig = new WebAppsApiClient.SiteConfigResource(); // SiteConfigResource | JSON representation of a SiteConfig object. See example.
apiInstance.webAppsUpdateConfigurationSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteConfig, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will update configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteConfig** | [**SiteConfigResource**](SiteConfigResource.md)| JSON representation of a SiteConfig object. See example. | 

### Return type

[**SiteConfigResource**](SiteConfigResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateConnectionStrings

> ConnectionStringDictionary webAppsUpdateConnectionStrings(resourceGroupName, name, subscriptionId, apiVersion, connectionStrings)

Replaces the connection strings of an app.

Replaces the connection strings of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionStrings = new WebAppsApiClient.ConnectionStringDictionary(); // ConnectionStringDictionary | Connection strings of the app or deployment slot. See example.
apiInstance.webAppsUpdateConnectionStrings(resourceGroupName, name, subscriptionId, apiVersion, connectionStrings, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionStrings** | [**ConnectionStringDictionary**](ConnectionStringDictionary.md)| Connection strings of the app or deployment slot. See example. | 

### Return type

[**ConnectionStringDictionary**](ConnectionStringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateConnectionStringsSlot

> ConnectionStringDictionary webAppsUpdateConnectionStringsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, connectionStrings)

Replaces the connection strings of an app.

Replaces the connection strings of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will update the connection settings for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionStrings = new WebAppsApiClient.ConnectionStringDictionary(); // ConnectionStringDictionary | Connection strings of the app or deployment slot. See example.
apiInstance.webAppsUpdateConnectionStringsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, connectionStrings, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will update the connection settings for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionStrings** | [**ConnectionStringDictionary**](ConnectionStringDictionary.md)| Connection strings of the app or deployment slot. See example. | 

### Return type

[**ConnectionStringDictionary**](ConnectionStringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateDiagnosticLogsConfig

> SiteLogsConfig webAppsUpdateDiagnosticLogsConfig(resourceGroupName, name, subscriptionId, apiVersion, siteLogsConfig)

Updates the logging configuration of an app.

Updates the logging configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteLogsConfig = new WebAppsApiClient.SiteLogsConfig(); // SiteLogsConfig | A SiteLogsConfig JSON object that contains the logging configuration to change in the \"properties\" property.
apiInstance.webAppsUpdateDiagnosticLogsConfig(resourceGroupName, name, subscriptionId, apiVersion, siteLogsConfig, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteLogsConfig** | [**SiteLogsConfig**](SiteLogsConfig.md)| A SiteLogsConfig JSON object that contains the logging configuration to change in the \&quot;properties\&quot; property. | 

### Return type

[**SiteLogsConfig**](SiteLogsConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateDiagnosticLogsConfigSlot

> SiteLogsConfig webAppsUpdateDiagnosticLogsConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteLogsConfig)

Updates the logging configuration of an app.

Updates the logging configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will update the logging configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteLogsConfig = new WebAppsApiClient.SiteLogsConfig(); // SiteLogsConfig | A SiteLogsConfig JSON object that contains the logging configuration to change in the \"properties\" property.
apiInstance.webAppsUpdateDiagnosticLogsConfigSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteLogsConfig, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will update the logging configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteLogsConfig** | [**SiteLogsConfig**](SiteLogsConfig.md)| A SiteLogsConfig JSON object that contains the logging configuration to change in the \&quot;properties\&quot; property. | 

### Return type

[**SiteLogsConfig**](SiteLogsConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateDomainOwnershipIdentifier

> WebAppsGetDomainOwnershipIdentifier200Response webAppsUpdateDomainOwnershipIdentifier(resourceGroupName, name, domainOwnershipIdentifierName, subscriptionId, apiVersion, domainOwnershipIdentifier)

Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let domainOwnershipIdentifierName = "domainOwnershipIdentifierName_example"; // String | Name of domain ownership identifier.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let domainOwnershipIdentifier = new WebAppsApiClient.WebAppsGetDomainOwnershipIdentifier200Response(); // WebAppsGetDomainOwnershipIdentifier200Response | A JSON representation of the domain ownership properties.
apiInstance.webAppsUpdateDomainOwnershipIdentifier(resourceGroupName, name, domainOwnershipIdentifierName, subscriptionId, apiVersion, domainOwnershipIdentifier, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **domainOwnershipIdentifierName** | **String**| Name of domain ownership identifier. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **domainOwnershipIdentifier** | [**WebAppsGetDomainOwnershipIdentifier200Response**](WebAppsGetDomainOwnershipIdentifier200Response.md)| A JSON representation of the domain ownership properties. | 

### Return type

[**WebAppsGetDomainOwnershipIdentifier200Response**](WebAppsGetDomainOwnershipIdentifier200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateDomainOwnershipIdentifierSlot

> WebAppsGetDomainOwnershipIdentifier200Response webAppsUpdateDomainOwnershipIdentifierSlot(resourceGroupName, name, domainOwnershipIdentifierName, slot, subscriptionId, apiVersion, domainOwnershipIdentifier)

Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let domainOwnershipIdentifierName = "domainOwnershipIdentifierName_example"; // String | Name of domain ownership identifier.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let domainOwnershipIdentifier = new WebAppsApiClient.WebAppsGetDomainOwnershipIdentifier200Response(); // WebAppsGetDomainOwnershipIdentifier200Response | A JSON representation of the domain ownership properties.
apiInstance.webAppsUpdateDomainOwnershipIdentifierSlot(resourceGroupName, name, domainOwnershipIdentifierName, slot, subscriptionId, apiVersion, domainOwnershipIdentifier, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **domainOwnershipIdentifierName** | **String**| Name of domain ownership identifier. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **domainOwnershipIdentifier** | [**WebAppsGetDomainOwnershipIdentifier200Response**](WebAppsGetDomainOwnershipIdentifier200Response.md)| A JSON representation of the domain ownership properties. | 

### Return type

[**WebAppsGetDomainOwnershipIdentifier200Response**](WebAppsGetDomainOwnershipIdentifier200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateHybridConnection

> WebAppsGetHybridConnection200Response webAppsUpdateHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion, connectionEnvelope)

Creates a new Hybrid Connection using a Service Bus relay.

Creates a new Hybrid Connection using a Service Bus relay.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let namespaceName = "namespaceName_example"; // String | The namespace for this hybrid connection.
let relayName = "relayName_example"; // String | The relay name for this hybrid connection.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.WebAppsGetHybridConnection200Response(); // WebAppsGetHybridConnection200Response | The details of the hybrid connection.
apiInstance.webAppsUpdateHybridConnection(resourceGroupName, name, namespaceName, relayName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **namespaceName** | **String**| The namespace for this hybrid connection. | 
 **relayName** | **String**| The relay name for this hybrid connection. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**WebAppsGetHybridConnection200Response**](WebAppsGetHybridConnection200Response.md)| The details of the hybrid connection. | 

### Return type

[**WebAppsGetHybridConnection200Response**](WebAppsGetHybridConnection200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateHybridConnectionSlot

> WebAppsGetHybridConnection200Response webAppsUpdateHybridConnectionSlot(resourceGroupName, name, namespaceName, relayName, slot, subscriptionId, apiVersion, connectionEnvelope)

Creates a new Hybrid Connection using a Service Bus relay.

Creates a new Hybrid Connection using a Service Bus relay.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | The name of the web app.
let namespaceName = "namespaceName_example"; // String | The namespace for this hybrid connection.
let relayName = "relayName_example"; // String | The relay name for this hybrid connection.
let slot = "slot_example"; // String | The name of the slot for the web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.WebAppsGetHybridConnection200Response(); // WebAppsGetHybridConnection200Response | The details of the hybrid connection.
apiInstance.webAppsUpdateHybridConnectionSlot(resourceGroupName, name, namespaceName, relayName, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| The name of the web app. | 
 **namespaceName** | **String**| The namespace for this hybrid connection. | 
 **relayName** | **String**| The relay name for this hybrid connection. | 
 **slot** | **String**| The name of the slot for the web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**WebAppsGetHybridConnection200Response**](WebAppsGetHybridConnection200Response.md)| The details of the hybrid connection. | 

### Return type

[**WebAppsGetHybridConnection200Response**](WebAppsGetHybridConnection200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateMetadata

> StringDictionary webAppsUpdateMetadata(resourceGroupName, name, subscriptionId, apiVersion, metadata)

Replaces the metadata of an app.

Replaces the metadata of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let metadata = new WebAppsApiClient.StringDictionary(); // StringDictionary | Edited metadata of the app or deployment slot. See example.
apiInstance.webAppsUpdateMetadata(resourceGroupName, name, subscriptionId, apiVersion, metadata, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **metadata** | [**StringDictionary**](StringDictionary.md)| Edited metadata of the app or deployment slot. See example. | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateMetadataSlot

> StringDictionary webAppsUpdateMetadataSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, metadata)

Replaces the metadata of an app.

Replaces the metadata of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will update the metadata for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let metadata = new WebAppsApiClient.StringDictionary(); // StringDictionary | Edited metadata of the app or deployment slot. See example.
apiInstance.webAppsUpdateMetadataSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, metadata, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will update the metadata for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **metadata** | [**StringDictionary**](StringDictionary.md)| Edited metadata of the app or deployment slot. See example. | 

### Return type

[**StringDictionary**](StringDictionary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdatePremierAddOn

> PremierAddOn webAppsUpdatePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion, premierAddOn)

Updates a named add-on of an app.

Updates a named add-on of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let premierAddOnName = "premierAddOnName_example"; // String | Add-on name.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let premierAddOn = new WebAppsApiClient.PremierAddOnPatchResource(); // PremierAddOnPatchResource | A JSON representation of the edited premier add-on.
apiInstance.webAppsUpdatePremierAddOn(resourceGroupName, name, premierAddOnName, subscriptionId, apiVersion, premierAddOn, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **premierAddOnName** | **String**| Add-on name. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **premierAddOn** | [**PremierAddOnPatchResource**](PremierAddOnPatchResource.md)| A JSON representation of the edited premier add-on. | 

### Return type

[**PremierAddOn**](PremierAddOn.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdatePremierAddOnSlot

> PremierAddOn webAppsUpdatePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion, premierAddOn)

Updates a named add-on of an app.

Updates a named add-on of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let premierAddOnName = "premierAddOnName_example"; // String | Add-on name.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will update the named add-on for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let premierAddOn = new WebAppsApiClient.PremierAddOnPatchResource(); // PremierAddOnPatchResource | A JSON representation of the edited premier add-on.
apiInstance.webAppsUpdatePremierAddOnSlot(resourceGroupName, name, premierAddOnName, slot, subscriptionId, apiVersion, premierAddOn, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **premierAddOnName** | **String**| Add-on name. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will update the named add-on for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **premierAddOn** | [**PremierAddOnPatchResource**](PremierAddOnPatchResource.md)| A JSON representation of the edited premier add-on. | 

### Return type

[**PremierAddOn**](PremierAddOn.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateRelayServiceConnection

> RelayServiceConnectionEntity webAppsUpdateRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, connectionEnvelope)

Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let entityName = "entityName_example"; // String | Name of the hybrid connection configuration.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.RelayServiceConnectionEntity(); // RelayServiceConnectionEntity | Details of the hybrid connection configuration.
apiInstance.webAppsUpdateRelayServiceConnection(resourceGroupName, name, entityName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **entityName** | **String**| Name of the hybrid connection configuration. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)| Details of the hybrid connection configuration. | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateRelayServiceConnectionSlot

> RelayServiceConnectionEntity webAppsUpdateRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, connectionEnvelope)

Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let entityName = "entityName_example"; // String | Name of the hybrid connection configuration.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will create or update a hybrid connection for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.RelayServiceConnectionEntity(); // RelayServiceConnectionEntity | Details of the hybrid connection configuration.
apiInstance.webAppsUpdateRelayServiceConnectionSlot(resourceGroupName, name, entityName, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **entityName** | **String**| Name of the hybrid connection configuration. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will create or update a hybrid connection for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)| Details of the hybrid connection configuration. | 

### Return type

[**RelayServiceConnectionEntity**](RelayServiceConnectionEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateSitePushSettings

> WebAppsUpdateSitePushSettingsRequest webAppsUpdateSitePushSettings(resourceGroupName, name, subscriptionId, apiVersion, pushSettings)

Updates the Push settings associated with web app.

Updates the Push settings associated with web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let pushSettings = new WebAppsApiClient.WebAppsUpdateSitePushSettingsRequest(); // WebAppsUpdateSitePushSettingsRequest | Push settings associated with web app.
apiInstance.webAppsUpdateSitePushSettings(resourceGroupName, name, subscriptionId, apiVersion, pushSettings, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **pushSettings** | [**WebAppsUpdateSitePushSettingsRequest**](WebAppsUpdateSitePushSettingsRequest.md)| Push settings associated with web app. | 

### Return type

[**WebAppsUpdateSitePushSettingsRequest**](WebAppsUpdateSitePushSettingsRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateSitePushSettingsSlot

> WebAppsUpdateSitePushSettingsRequest webAppsUpdateSitePushSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, pushSettings)

Updates the Push settings associated with web app.

Updates the Push settings associated with web app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of web app.
let slot = "slot_example"; // String | Name of web app slot. If not specified then will default to production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let pushSettings = new WebAppsApiClient.WebAppsUpdateSitePushSettingsRequest(); // WebAppsUpdateSitePushSettingsRequest | Push settings associated with web app.
apiInstance.webAppsUpdateSitePushSettingsSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, pushSettings, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of web app. | 
 **slot** | **String**| Name of web app slot. If not specified then will default to production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **pushSettings** | [**WebAppsUpdateSitePushSettingsRequest**](WebAppsUpdateSitePushSettingsRequest.md)| Push settings associated with web app. | 

### Return type

[**WebAppsUpdateSitePushSettingsRequest**](WebAppsUpdateSitePushSettingsRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateSlot

> WebAppsGet200Response webAppsUpdateSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteEnvelope)

Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Unique name of the app to create or update. To create or update a deployment slot, use the {slot} parameter.
let slot = "slot_example"; // String | Name of the deployment slot to create or update. By default, this API attempts to create or modify the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteEnvelope = new WebAppsApiClient.SitePatchResource(); // SitePatchResource | A JSON representation of the app properties. See example.
apiInstance.webAppsUpdateSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Unique name of the app to create or update. To create or update a deployment slot, use the {slot} parameter. | 
 **slot** | **String**| Name of the deployment slot to create or update. By default, this API attempts to create or modify the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteEnvelope** | [**SitePatchResource**](SitePatchResource.md)| A JSON representation of the app properties. See example. | 

### Return type

[**WebAppsGet200Response**](WebAppsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateSlotConfigurationNames

> SlotConfigNamesResource webAppsUpdateSlotConfigurationNames(resourceGroupName, name, subscriptionId, apiVersion, slotConfigNames)

Updates the names of application settings and connection string that remain with the slot during swap operation.

Updates the names of application settings and connection string that remain with the slot during swap operation.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let slotConfigNames = new WebAppsApiClient.SlotConfigNamesResource(); // SlotConfigNamesResource | Names of application settings and connection strings. See example.
apiInstance.webAppsUpdateSlotConfigurationNames(resourceGroupName, name, subscriptionId, apiVersion, slotConfigNames, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **slotConfigNames** | [**SlotConfigNamesResource**](SlotConfigNamesResource.md)| Names of application settings and connection strings. See example. | 

### Return type

[**SlotConfigNamesResource**](SlotConfigNamesResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateSourceControl

> SiteSourceControl webAppsUpdateSourceControl(resourceGroupName, name, subscriptionId, apiVersion, siteSourceControl)

Updates the source control configuration of an app.

Updates the source control configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteSourceControl = new WebAppsApiClient.SiteSourceControl(); // SiteSourceControl | JSON representation of a SiteSourceControl object. See example.
apiInstance.webAppsUpdateSourceControl(resourceGroupName, name, subscriptionId, apiVersion, siteSourceControl, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteSourceControl** | [**SiteSourceControl**](SiteSourceControl.md)| JSON representation of a SiteSourceControl object. See example. | 

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateSourceControlSlot

> SiteSourceControl webAppsUpdateSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteSourceControl)

Updates the source control configuration of an app.

Updates the source control configuration of an app.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will update the source control configuration for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let siteSourceControl = new WebAppsApiClient.SiteSourceControl(); // SiteSourceControl | JSON representation of a SiteSourceControl object. See example.
apiInstance.webAppsUpdateSourceControlSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, siteSourceControl, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will update the source control configuration for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **siteSourceControl** | [**SiteSourceControl**](SiteSourceControl.md)| JSON representation of a SiteSourceControl object. See example. | 

### Return type

[**SiteSourceControl**](SiteSourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateSwiftVirtualNetworkConnection

> SwiftVirtualNetwork webAppsUpdateSwiftVirtualNetworkConnection(resourceGroupName, name, subscriptionId, apiVersion, connectionEnvelope)

Integrates this Web App with a Virtual Network. This requires that 1) \&quot;swiftSupported\&quot; is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not  in use by another App Service Plan other than the one this App is in.

Integrates this Web App with a Virtual Network. This requires that 1) \&quot;swiftSupported\&quot; is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.SwiftVirtualNetwork(); // SwiftVirtualNetwork | Properties of the Virtual Network connection. See example.
apiInstance.webAppsUpdateSwiftVirtualNetworkConnection(resourceGroupName, name, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**SwiftVirtualNetwork**](SwiftVirtualNetwork.md)| Properties of the Virtual Network connection. See example. | 

### Return type

[**SwiftVirtualNetwork**](SwiftVirtualNetwork.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateSwiftVirtualNetworkConnectionSlot

> SwiftVirtualNetwork webAppsUpdateSwiftVirtualNetworkConnectionSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, connectionEnvelope)

Integrates this Web App with a Virtual Network. This requires that 1) \&quot;swiftSupported\&quot; is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not  in use by another App Service Plan other than the one this App is in.

Integrates this Web App with a Virtual Network. This requires that 1) \&quot;swiftSupported\&quot; is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in.

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will add or update connections for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.SwiftVirtualNetwork(); // SwiftVirtualNetwork | Properties of the Virtual Network connection. See example.
apiInstance.webAppsUpdateSwiftVirtualNetworkConnectionSlot(resourceGroupName, name, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will add or update connections for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**SwiftVirtualNetwork**](SwiftVirtualNetwork.md)| Properties of the Virtual Network connection. See example. | 

### Return type

[**SwiftVirtualNetwork**](SwiftVirtualNetwork.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateVnetConnection

> WebAppsGetVnetConnectionSlot200Response webAppsUpdateVnetConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, connectionEnvelope)

Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let vnetName = "vnetName_example"; // String | Name of an existing Virtual Network.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.WebAppsGetVnetConnectionSlot200Response(); // WebAppsGetVnetConnectionSlot200Response | Properties of the Virtual Network connection. See example.
apiInstance.webAppsUpdateVnetConnection(resourceGroupName, name, vnetName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **vnetName** | **String**| Name of an existing Virtual Network. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**WebAppsGetVnetConnectionSlot200Response**](WebAppsGetVnetConnectionSlot200Response.md)| Properties of the Virtual Network connection. See example. | 

### Return type

[**WebAppsGetVnetConnectionSlot200Response**](WebAppsGetVnetConnectionSlot200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateVnetConnectionGateway

> WebAppsGetVnetConnectionGatewaySlot200Response webAppsUpdateVnetConnectionGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope)

Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let vnetName = "vnetName_example"; // String | Name of the Virtual Network.
let gatewayName = "gatewayName_example"; // String | Name of the gateway. Currently, the only supported string is \"primary\".
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.WebAppsGetVnetConnectionGatewaySlot200Response(); // WebAppsGetVnetConnectionGatewaySlot200Response | The properties to update this gateway with.
apiInstance.webAppsUpdateVnetConnectionGateway(resourceGroupName, name, vnetName, gatewayName, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **vnetName** | **String**| Name of the Virtual Network. | 
 **gatewayName** | **String**| Name of the gateway. Currently, the only supported string is \&quot;primary\&quot;. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**WebAppsGetVnetConnectionGatewaySlot200Response**](WebAppsGetVnetConnectionGatewaySlot200Response.md)| The properties to update this gateway with. | 

### Return type

[**WebAppsGetVnetConnectionGatewaySlot200Response**](WebAppsGetVnetConnectionGatewaySlot200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateVnetConnectionGatewaySlot

> WebAppsGetVnetConnectionGatewaySlot200Response webAppsUpdateVnetConnectionGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion, connectionEnvelope)

Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let vnetName = "vnetName_example"; // String | Name of the Virtual Network.
let gatewayName = "gatewayName_example"; // String | Name of the gateway. Currently, the only supported string is \"primary\".
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will add or update a gateway for the production slot's Virtual Network.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.WebAppsGetVnetConnectionGatewaySlot200Response(); // WebAppsGetVnetConnectionGatewaySlot200Response | The properties to update this gateway with.
apiInstance.webAppsUpdateVnetConnectionGatewaySlot(resourceGroupName, name, vnetName, gatewayName, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **vnetName** | **String**| Name of the Virtual Network. | 
 **gatewayName** | **String**| Name of the gateway. Currently, the only supported string is \&quot;primary\&quot;. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will add or update a gateway for the production slot&#39;s Virtual Network. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**WebAppsGetVnetConnectionGatewaySlot200Response**](WebAppsGetVnetConnectionGatewaySlot200Response.md)| The properties to update this gateway with. | 

### Return type

[**WebAppsGetVnetConnectionGatewaySlot200Response**](WebAppsGetVnetConnectionGatewaySlot200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webAppsUpdateVnetConnectionSlot

> WebAppsGetVnetConnectionSlot200Response webAppsUpdateVnetConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, connectionEnvelope)

Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

### Example

```javascript
import WebAppsApiClient from 'web_apps_api_client';
let defaultClient = WebAppsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebAppsApiClient.WebAppsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Name of the app.
let vnetName = "vnetName_example"; // String | Name of an existing Virtual Network.
let slot = "slot_example"; // String | Name of the deployment slot. If a slot is not specified, the API will add or update connections for the production slot.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let connectionEnvelope = new WebAppsApiClient.WebAppsGetVnetConnectionSlot200Response(); // WebAppsGetVnetConnectionSlot200Response | Properties of the Virtual Network connection. See example.
apiInstance.webAppsUpdateVnetConnectionSlot(resourceGroupName, name, vnetName, slot, subscriptionId, apiVersion, connectionEnvelope, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Name of the app. | 
 **vnetName** | **String**| Name of an existing Virtual Network. | 
 **slot** | **String**| Name of the deployment slot. If a slot is not specified, the API will add or update connections for the production slot. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **connectionEnvelope** | [**WebAppsGetVnetConnectionSlot200Response**](WebAppsGetVnetConnectionSlot200Response.md)| Properties of the Virtual Network connection. See example. | 

### Return type

[**WebAppsGetVnetConnectionSlot200Response**](WebAppsGetVnetConnectionSlot200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

