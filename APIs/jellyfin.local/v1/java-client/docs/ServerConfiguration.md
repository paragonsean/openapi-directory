

# ServerConfiguration

Represents the server configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityLogRetentionDays** | **Integer** | Gets or sets the number of days we should retain activity logs. |  [optional] |
|**autoDiscovery** | **Boolean** | Gets or sets a value indicating whether Autodiscovery is enabled. |  [optional] |
|**autoDiscoveryTracing** | **Boolean** | Gets or sets a value indicating whether Autodiscovery tracing is enabled. |  [optional] |
|**baseUrl** | **String** |  |  [optional] |
|**cachePath** | **String** | Gets or sets the cache path. |  [optional] |
|**certificatePassword** | **String** | Gets or sets the password required to access the X.509 certificate data in the file specified by MediaBrowser.Model.Configuration.ServerConfiguration.CertificatePath. |  [optional] |
|**certificatePath** | **String** | Gets or sets the filesystem path of an X.509 certificate to use for SSL. |  [optional] |
|**codecsUsed** | **List&lt;String&gt;** |  |  [optional] |
|**contentTypes** | [**List&lt;NameValuePair&gt;**](NameValuePair.md) |  |  [optional] |
|**corsHosts** | **List&lt;String&gt;** | Gets or sets the cors hosts. |  [optional] |
|**disableLiveTvChannelUserDataName** | **Boolean** |  |  [optional] |
|**disablePluginImages** | **Boolean** | Gets or sets a value indicating whether plugin image should be disabled. |  [optional] |
|**displaySpecialsWithinSeasons** | **Boolean** |  |  [optional] |
|**enableCaseSensitiveItemIds** | **Boolean** | Gets or sets a value indicating whether [enable case sensitive item ids]. |  [optional] |
|**enableDashboardResponseCaching** | **Boolean** | Gets or sets a value indicating whether [enable dashboard response caching].  Allows potential contributors without visual studio to modify production dashboard code and test changes. |  [optional] |
|**enableExternalContentInSuggestions** | **Boolean** |  |  [optional] |
|**enableFolderView** | **Boolean** |  |  [optional] |
|**enableGroupingIntoCollections** | **Boolean** |  |  [optional] |
|**enableHttps** | **Boolean** | Gets or sets a value indicating whether to use HTTPS. |  [optional] |
|**enableIPV4** | **Boolean** | Gets or sets a value indicating whether IPV4 capability is enabled. |  [optional] |
|**enableIPV6** | **Boolean** | Gets or sets a value indicating whether IPV6 capability is enabled. |  [optional] |
|**enableMetrics** | **Boolean** | Gets or sets a value indicating whether to enable prometheus metrics exporting. |  [optional] |
|**enableMultiSocketBinding** | **Boolean** | Gets a value indicating whether multi-socket binding is available. |  [optional] [readonly] |
|**enableNewOmdbSupport** | **Boolean** |  |  [optional] |
|**enableNormalizedItemByNameIds** | **Boolean** |  |  [optional] |
|**enableRemoteAccess** | **Boolean** | Gets or sets a value indicating whether access outside of the LAN is permitted. |  [optional] |
|**enableSSDPTracing** | **Boolean** | Gets or sets a value indicating whether detailed ssdp logs are sent to the console/log.  \&quot;Emby.Dlna\&quot;: \&quot;Debug\&quot; must be set in logging.default.json for this property to work. |  [optional] |
|**enableSimpleArtistDetection** | **Boolean** |  |  [optional] |
|**enableSlowResponseWarning** | **Boolean** | Gets or sets a value indicating whether slow server responses should be logged as a warning. |  [optional] |
|**enableUPnP** | **Boolean** | Gets or sets a value indicating whether to enable automatic port forwarding. |  [optional] |
|**gatewayMonitorPeriod** | **Integer** | Gets or sets the time (in seconds) between the pings of SSDP gateway monitor. |  [optional] |
|**hdHomerunPortRange** | **String** | Gets or sets the ports that HDHomerun uses. |  [optional] |
|**httpServerPortNumber** | **Integer** | Gets or sets the HTTP server port number. |  [optional] |
|**httpsPortNumber** | **Integer** | Gets or sets the HTTPS server port number. |  [optional] |
|**ignoreVirtualInterfaces** | **Boolean** | Gets or sets a value indicating whether address names that match MediaBrowser.Model.Configuration.ServerConfiguration.VirtualInterfaceNames should be Ignore for the purposes of binding. |  [optional] |
|**imageExtractionTimeoutMs** | **Integer** |  |  [optional] |
|**imageSavingConvention** | **ImageSavingConvention** |  |  [optional] |
|**isPortAuthorized** | **Boolean** | Gets or sets a value indicating whether this instance is port authorized. |  [optional] |
|**isRemoteIPFilterBlacklist** | **Boolean** | Gets or sets a value indicating whether &lt;seealso cref&#x3D;\&quot;P:MediaBrowser.Model.Configuration.ServerConfiguration.RemoteIPFilter\&quot; /&gt; contains a blacklist or a whitelist. Default is a whitelist. |  [optional] |
|**isStartupWizardCompleted** | **Boolean** | Gets or sets a value indicating whether this instance is first run. |  [optional] |
|**knownProxies** | **List&lt;String&gt;** | Gets or sets the known proxies. |  [optional] |
|**libraryMetadataRefreshConcurrency** | **Integer** | Gets or sets the how many metadata refreshes can run concurrently. |  [optional] |
|**libraryMonitorDelay** | **Integer** | Gets or sets the delay in seconds that we will wait after a file system change to try and discover what has been added/removed  Some delay is necessary with some items because their creation is not atomic.  It involves the creation of several  different directories and files. |  [optional] |
|**libraryScanFanoutConcurrency** | **Integer** | Gets or sets the how the library scan fans out. |  [optional] |
|**localNetworkAddresses** | **List&lt;String&gt;** | Gets or sets the interface addresses which Jellyfin will bind to. If empty, all interfaces will be used. |  [optional] |
|**localNetworkSubnets** | **List&lt;String&gt;** | Gets or sets the subnets that are deemed to make up the LAN. |  [optional] |
|**logFileRetentionDays** | **Integer** | Gets or sets the number of days we should retain log files. |  [optional] |
|**maxAudiobookResume** | **Integer** | Gets or sets the remaining minutes of a book that can be played while still saving playstate. If this percentage is crossed playstate will be reset to the beginning and the item will be marked watched. |  [optional] |
|**maxResumePct** | **Integer** | Gets or sets the maximum percentage of an item that can be played while still saving playstate. If this percentage is crossed playstate will be reset to the beginning and the item will be marked watched. |  [optional] |
|**metadataCountryCode** | **String** | Gets or sets the metadata country code. |  [optional] |
|**metadataNetworkPath** | **String** |  |  [optional] |
|**metadataOptions** | [**List&lt;MetadataOptions&gt;**](MetadataOptions.md) |  |  [optional] |
|**metadataPath** | **String** | Gets or sets the metadata path. |  [optional] |
|**minAudiobookResume** | **Integer** | Gets or sets the minimum minutes of a book that must be played in order for playstate to be updated. |  [optional] |
|**minResumeDurationSeconds** | **Integer** | Gets or sets the minimum duration that an item must have in order to be eligible for playstate updates.. |  [optional] |
|**minResumePct** | **Integer** | Gets or sets the minimum percentage of an item that must be played in order for playstate to be updated. |  [optional] |
|**pathSubstitutions** | [**List&lt;PathSubstitution&gt;**](PathSubstitution.md) |  |  [optional] |
|**pluginRepositories** | [**List&lt;RepositoryInfo&gt;**](RepositoryInfo.md) |  |  [optional] |
|**preferredMetadataLanguage** | **String** | Gets or sets the preferred metadata language. |  [optional] |
|**previousVersion** | [**Version**](Version.md) |  |  [optional] |
|**previousVersionStr** | **String** | Gets or sets the stringified PreviousVersion to be stored/loaded,  because System.Version itself isn&#39;t xml-serializable. |  [optional] |
|**publicHttpsPort** | **Integer** | Gets or sets the public HTTPS port. |  [optional] |
|**publicPort** | **Integer** | Gets or sets the public mapped port. |  [optional] |
|**publishedServerUriBySubnet** | **List&lt;String&gt;** | Gets or sets PublishedServerUri to advertise for specific subnets. |  [optional] |
|**quickConnectAvailable** | **Boolean** | Gets or sets a value indicating whether quick connect is available for use on this server. |  [optional] |
|**remoteClientBitrateLimit** | **Integer** |  |  [optional] |
|**remoteIPFilter** | **List&lt;String&gt;** | Gets or sets the filter for remote IP connectivity. Used in conjuntion with &lt;seealso cref&#x3D;\&quot;P:MediaBrowser.Model.Configuration.ServerConfiguration.IsRemoteIPFilterBlacklist\&quot; /&gt;. |  [optional] |
|**removeOldPlugins** | **Boolean** | Gets or sets a value indicating whether older plugins should automatically be deleted from the plugin folder. |  [optional] |
|**requireHttps** | **Boolean** | Gets or sets a value indicating whether the server should force connections over HTTPS. |  [optional] |
|**ssDPTracingFilter** | **String** | Gets or sets a value indicating whether an IP address is to be used to filter the detailed ssdp logs that are being sent to the console/log.  If the setting \&quot;Emby.Dlna\&quot;: \&quot;Debug\&quot; msut be set in logging.default.json for this property to work. |  [optional] |
|**saveMetadataHidden** | **Boolean** |  |  [optional] |
|**serverName** | **String** |  |  [optional] |
|**skipDeserializationForBasicTypes** | **Boolean** |  |  [optional] |
|**slowResponseThresholdMs** | **Long** | Gets or sets the threshold for the slow response time warning in ms. |  [optional] |
|**sortRemoveCharacters** | **List&lt;String&gt;** | Gets or sets characters to be removed from strings to create a sort name. |  [optional] |
|**sortRemoveWords** | **List&lt;String&gt;** | Gets or sets words to be removed from strings to create a sort name. |  [optional] |
|**sortReplaceCharacters** | **List&lt;String&gt;** | Gets or sets characters to be replaced with a &#39; &#39; in strings to create a sort name. |  [optional] |
|**trustAllIP6Interfaces** | **Boolean** | Gets or sets a value indicating whether all IPv6 interfaces should be treated as on the internal network.  Depending on the address range implemented ULA ranges might not be used. |  [optional] |
|**udPPortRange** | **String** | Gets or sets client udp port range. |  [optional] |
|**udPSendCount** | **Integer** | Gets or sets the number of times SSDP UDP messages are sent. |  [optional] |
|**udPSendDelay** | **Integer** | Gets or sets the delay between each groups of SSDP messages (in ms). |  [optional] |
|**uiCulture** | **String** |  |  [optional] |
|**upnPCreateHttpPortMap** | **Boolean** | Gets or sets a value indicating whether the http port should be mapped as part of UPnP automatic port forwarding. |  [optional] |
|**uninstalledPlugins** | **List&lt;String&gt;** |  |  [optional] |
|**virtualInterfaceNames** | **String** | Gets or sets a value indicating the interfaces that should be ignored. The list can be comma separated. &lt;seealso cref&#x3D;\&quot;P:MediaBrowser.Model.Configuration.ServerConfiguration.IgnoreVirtualInterfaces\&quot; /&gt;. |  [optional] |



