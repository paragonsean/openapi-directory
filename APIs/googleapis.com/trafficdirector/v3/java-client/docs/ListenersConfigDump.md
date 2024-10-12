

# ListenersConfigDump

Envoy's listener manager fills this message with all currently known listeners. Listener configuration information can be used to recreate an Envoy configuration by populating all listeners as static listeners or by returning them in a LDS response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dynamicListeners** | [**List&lt;DynamicListener&gt;**](DynamicListener.md) | State for any warming, active, or draining listeners. |  [optional] |
|**staticListeners** | [**List&lt;StaticListener&gt;**](StaticListener.md) | The statically loaded listener configs. |  [optional] |
|**versionInfo** | **String** | This is the :ref:&#x60;version_info &#x60; in the last processed LDS discovery response. If there are only static bootstrap listeners, this field will be \&quot;\&quot;. |  [optional] |



