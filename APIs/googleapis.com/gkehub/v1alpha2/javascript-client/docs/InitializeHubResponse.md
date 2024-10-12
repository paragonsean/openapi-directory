# GkeHubApi.InitializeHubResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serviceIdentity** | **String** | Name of the Hub default service identity, in the format: service-@gcp-sa-gkehub.iam.gserviceaccount.com The service account has &#x60;roles/gkehub.serviceAgent&#x60; in the Hub project. | [optional] 
**workloadIdentityPool** | **String** | The Workload Identity Pool used for Workload Identity-enabled clusters registered with this Hub. Format: &#x60;.hub.id.goog&#x60; | [optional] 


