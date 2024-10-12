

# UpdateStoreRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**UpdatableAddress**](UpdatableAddress.md) | The address of the store. It is not possible to update the country of the store. |  [optional] |
|**businessLineIds** | **List&lt;String&gt;** | The unique identifiers of the [business lines](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines__resParam_id) that the store is associated with. |  [optional] |
|**description** | **String** | The description of the store. |  [optional] |
|**externalReferenceId** | **String** | The unique identifier of the store, used by certain payment methods and tax authorities. Accepts up to 14 digits.  Required for CNPJ in Brazil, in the format 00.000.000/00git00-00 separated by dots, slashes, hyphens, or without separators.  Optional for Zip in Australia and SIRET in France, required except for nonprofit organizations and incorporated associations.   |  [optional] |
|**phoneNumber** | **String** | The phone number of the store, including &#39;+&#39; and country code in the [E.164](https://en.wikipedia.org/wiki/E.164) format. If passed in a different format, we convert and validate the phone number against E.164.  |  [optional] |
|**splitConfiguration** | [**StoreSplitConfiguration**](StoreSplitConfiguration.md) | Rules for Adyen for Platforms merchants to split the transaction amount and fees. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the store. Possible values are:  - **active**: This value is assigned automatically when a store is created.  - **inactive**: The maximum [transaction limits and number of Store-and-Forward transactions](https://docs.adyen.com/point-of-sale/determine-account-structure/configure-features#payment-features) for the store are set to 0. This blocks new transactions, but captures are still possible. - **closed**: The terminals of the store are reassigned to the merchant inventory, so they can&#39;t process payments.  You can change the status from **active** to **inactive**, and from **inactive** to **active** or **closed**.  Once **closed**, a store can&#39;t be reopened. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| CLOSED | &quot;closed&quot; |
| INACTIVE | &quot;inactive&quot; |



