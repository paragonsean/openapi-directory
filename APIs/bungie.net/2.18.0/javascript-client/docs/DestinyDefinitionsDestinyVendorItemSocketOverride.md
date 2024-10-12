# BungieNetApi.DestinyDefinitionsDestinyVendorItemSocketOverride

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**randomizedOptionsCount** | **Number** | If this is greater than -1, the number of randomized plugs on this socket will be set to this quantity instead of whatever it&#39;s set to by default. | [optional] 
**singleItemHash** | **Number** | If this is populated, the socket will be overridden with a specific plug.  If this isn&#39;t populated, it&#39;s being overridden by something more complicated that is only known by the Game Server and God, which means we can&#39;t tell you in advance what it&#39;ll be. | [optional] 
**socketTypeHash** | **Number** | This appears to be used to select which socket ultimately gets the override defined here. | [optional] 


