

# PaymentConfiguration

Payment Configuration object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowInstallmentsMerge** | **Boolean** | By default (when &#x60;false&#x60;), on a multi-seller purchase is on the run, a simple intersection with installments options configured by every seller will be available. When &#x60;true&#x60;, this option allows a more complex but flexible installment option, since it considers max installments of every seller configuration, even if those don&#39;t match. Installment values ​​may not be equal in this case. |  [optional] |
|**requiresAuthenticationForPreAuthorizedPaymentOption** | **Boolean** | Determines whether pre-authorized payments require authentication |  |



