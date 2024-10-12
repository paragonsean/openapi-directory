

# V1Beta1ProducerQuotaPolicy

Quota policy created by service producer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**container** | **String** | The cloud resource container at which the quota policy is created. The format is {container_type}/{container_number} |  [optional] |
|**dimensions** | **Map&lt;String, String&gt;** |  If this map is nonempty, then this policy applies only to specific values for dimensions defined in the limit unit. For example, a policy on a limit with the unit 1/{project}/{region} could contain an entry with the key \&quot;region\&quot; and the value \&quot;us-east-1\&quot;; the policy is only applied to quota consumed in that region. This map has the following restrictions: * Keys that are not defined in the limit&#39;s unit are not valid keys. Any string appearing in {brackets} in the unit (besides {project} or {user}) is a defined key. * \&quot;project\&quot; is not a valid key; the project is already specified in the parent resource name. * \&quot;user\&quot; is not a valid key; the API does not support quota polcies that apply only to a specific user. * If \&quot;region\&quot; appears as a key, its value must be a valid Cloud region. * If \&quot;zone\&quot; appears as a key, its value must be a valid Cloud zone. * If any valid key other than \&quot;region\&quot; or \&quot;zone\&quot; appears in the map, then all valid keys other than \&quot;region\&quot; or \&quot;zone\&quot; must also appear in the map. |  [optional] |
|**metric** | **String** | The name of the metric to which this policy applies. An example name would be: &#x60;compute.googleapis.com/cpus&#x60; |  [optional] |
|**name** | **String** | The resource name of the producer policy. An example name would be: &#x60;services/compute.googleapis.com/organizations/123/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion/producerQuotaPolicies/4a3f2c1d&#x60; |  [optional] |
|**policyValue** | **String** | The quota policy value. Can be any nonnegative integer, or -1 (unlimited quota). |  [optional] |
|**unit** | **String** | The limit unit of the limit to which this policy applies. An example unit would be: &#x60;1/{project}/{region}&#x60; Note that &#x60;{project}&#x60; and &#x60;{region}&#x60; are not placeholders in this example; the literal characters &#x60;{&#x60; and &#x60;}&#x60; occur in the string. |  [optional] |



