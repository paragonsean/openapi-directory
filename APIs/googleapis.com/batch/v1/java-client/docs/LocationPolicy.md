

# LocationPolicy


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedLocations** | **List&lt;String&gt;** | A list of allowed location names represented by internal URLs. Each location can be a region or a zone. Only one region or multiple zones in one region is supported now. For example, [\&quot;regions/us-central1\&quot;] allow VMs in any zones in region us-central1. [\&quot;zones/us-central1-a\&quot;, \&quot;zones/us-central1-c\&quot;] only allow VMs in zones us-central1-a and us-central1-c. All locations end up in different regions would cause errors. For example, [\&quot;regions/us-central1\&quot;, \&quot;zones/us-central1-a\&quot;, \&quot;zones/us-central1-b\&quot;, \&quot;zones/us-west1-a\&quot;] contains 2 regions \&quot;us-central1\&quot; and \&quot;us-west1\&quot;. An error is expected in this case. |  [optional] |



