

# Invoice


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountDue** | **Integer** | Amount due set in invoice. |  |
|**applicationFee** | **Integer** | Application fee set in invoice. |  [optional] |
|**attemptCount** | **Integer** | Number of attempts to deliver invoice. |  [optional] |
|**attempted** | **Boolean** | Boolean to determine whether delivery attempt executed, or not. |  [optional] |
|**closed** | **Boolean** | Invoice closed, or pending. |  [optional] |
|**created** | **String** | Date and time when invoice was created. |  |
|**currency** | **String** | Currency used in invoice. |  |
|**customer** | **String** | Customer name. |  |
|**description** | **String** | Invoice description. |  [optional] |
|**id** | **String** | Invoice unique identifier expressed as UUID. |  [optional] |
|**invoiceDate** | **String** | Invoice issue date. |  |
|**livemode** | **Boolean** | Boolean that determines whether invoice is live, or not. |  [optional] |
|**metadata** | **Object** | Optional metadata object of invoice. |  [optional] |
|**nextPaymentAttempt** | **String** | Next payment attempt. |  [optional] |
|**paid** | **Boolean** | Determines whether invoice has been paid, or not. |  [optional] |
|**periodEnd** | **String** | Invoice end period. |  |
|**periodStart** | **String** | Invoice start period. |  |
|**recieptNumber** | **String** | Invoice receipt number. |  |
|**startingBalance** | **Integer** | Invoice starting balance. |  |
|**statementDescriptor** | **String** | Invoice statement descriptor. |  [optional] |
|**stripeId** | **String** | Stripe account identifier. |  |
|**subscription** | **String** | Suscription name. |  [optional] |
|**subtotal** | **Integer** | Invoice sub total. |  |
|**tax** | **Integer** | Tax, if applicable. |  [optional] |
|**total** | **Integer** | Invoice total. |  |



