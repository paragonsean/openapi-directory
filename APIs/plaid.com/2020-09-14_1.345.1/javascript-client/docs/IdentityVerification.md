# ThePlaidApi.IdentityVerification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientUserId** | **String** | An identifier to help you connect this object to your internal systems. For example, your database ID corresponding to this object. | 
**completedAt** | **Date** | An ISO8601 formatted timestamp. | 
**createdAt** | **Date** | An ISO8601 formatted timestamp. | 
**documentaryVerification** | [**DocumentaryVerification**](DocumentaryVerification.md) |  | 
**id** | **String** | ID of the associated Identity Verification attempt. | 
**kycCheck** | [**KYCCheckDetails**](KYCCheckDetails.md) |  | 
**previousAttemptId** | **String** | The ID for the Identity Verification preceding this session. This field will only be filled if the current Identity Verification is a retry of a previous attempt. | 
**redactedAt** | **Date** | An ISO8601 formatted timestamp. | 
**riskCheck** | [**RiskCheckDetails**](RiskCheckDetails.md) |  | 
**shareableUrl** | **String** | A shareable URL that can be sent directly to the user to complete verification | 
**status** | [**IdentityVerificationStatus**](IdentityVerificationStatus.md) |  | 
**steps** | [**IdentityVerificationStepSummary**](IdentityVerificationStepSummary.md) |  | 
**template** | [**IdentityVerificationTemplateReference**](IdentityVerificationTemplateReference.md) |  | 
**user** | [**IdentityVerificationUserData**](IdentityVerificationUserData.md) |  | 
**watchlistScreeningId** | **String** | ID of the associated screening. | 


