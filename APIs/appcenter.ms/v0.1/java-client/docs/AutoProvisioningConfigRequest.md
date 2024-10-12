

# AutoProvisioningConfigRequest

A request containing information for creating a Auto Provisioning Config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowAutoProvisioning** | **Boolean** | When *true* enables auto provisioning |  [optional] |
|**appleDeveloperAccountKey** | **String** | A key to a secret in customer-credential-store. apple_developer_account refers to the user&#39;s developer account that is used to log into https://developer.apple.com. Normally the user&#39;s email. |  [optional] |
|**appleDistributionCertificateKey** | **String** | A key to a secret in customer-credential-store. distribution_certificate refers to the customer&#39;s certificate (that holds the private key) that will be used to sign the app. |  [optional] |



