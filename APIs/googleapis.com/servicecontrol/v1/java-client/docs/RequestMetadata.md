

# RequestMetadata

Metadata about the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callerIp** | **String** | The IP address of the caller. For a caller from the internet, this will be the public IPv4 or IPv6 address. For calls made from inside Google&#39;s internal production network from one GCP service to another, &#x60;caller_ip&#x60; will be redacted to \&quot;private\&quot;. For a caller from a Compute Engine VM with a external IP address, &#x60;caller_ip&#x60; will be the VM&#39;s external IP address. For a caller from a Compute Engine VM without a external IP address, if the VM is in the same organization (or project) as the accessed resource, &#x60;caller_ip&#x60; will be the VM&#39;s internal IPv4 address, otherwise &#x60;caller_ip&#x60; will be redacted to \&quot;gce-internal-ip\&quot;. See https://cloud.google.com/compute/docs/vpc/ for more information. |  [optional] |
|**callerNetwork** | **String** | The network of the caller. Set only if the network host project is part of the same GCP organization (or project) as the accessed resource. See https://cloud.google.com/compute/docs/vpc/ for more information. This is a scheme-less URI full resource name. For example: \&quot;//compute.googleapis.com/projects/PROJECT_ID/global/networks/NETWORK_ID\&quot; |  [optional] |
|**callerSuppliedUserAgent** | **String** | The user agent of the caller. This information is not authenticated and should be treated accordingly. For example: + &#x60;google-api-python-client/1.4.0&#x60;: The request was made by the Google API client for Python. + &#x60;Cloud SDK Command Line Tool apitools-client/1.0 gcloud/0.9.62&#x60;: The request was made by the Google Cloud SDK CLI (gcloud). + &#x60;AppEngine-Google; (+http://code.google.com/appengine; appid: s~my-project&#x60;: The request was made from the &#x60;my-project&#x60; App Engine app. |  [optional] |
|**destinationAttributes** | [**Peer**](Peer.md) |  |  [optional] |
|**requestAttributes** | [**Request**](Request.md) |  |  [optional] |



