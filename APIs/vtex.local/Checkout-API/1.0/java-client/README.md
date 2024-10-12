# openapi-java-client

Checkout API
- API version: 1.0
  - Build date: 2024-10-12T11:55:50.715443-04:00[America/New_York]
  - Generator version: 7.9.0

>ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.

The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.

>ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.

>⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.

## Shopping cart

Allows merchants to simulate, configure and customize shopping cart information.

- [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)
- [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)
- [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)
- [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)
- [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)
- [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)
- [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)
- [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)
- [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)
- [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)
- [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)


## Cart attachments

Allows merchants to obtain client profiles and add information to a given shopping cart.

- [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)
- [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)
- [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)
- [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)
- [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)
- [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)
- [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)


## Custom data

Allows merchants to manage custom fields that were created by an app in their account.

- [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)
- [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)
- [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)


## Configuration

Allows merchants to configure orderForm in the account and seller exchange on a given order.

- [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)
- [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)
- [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)
- [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)
- [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)


## Fulfillment

Allows merchants to obtain pickup points and address information.

- [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)
- [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)


## Order placement

Allows merchants to place and process orders by creating a new cart or using an existing cart.

- [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)
- [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)
- [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)


## Region

Allows merchants to obtain a list of sellers serving a specific delivery region.

- [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)


*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>1.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:1.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-1.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.model.*;
import org.openapitools.client.api.CartAttachmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    CartAttachmentsApi apiInstance = new CartAttachmentsApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String orderFormId = "orderFormId_example"; // String | ID of the orderForm that will receive client profile information.
    AddClientPreferencesRequest addClientPreferencesRequest = new AddClientPreferencesRequest(); // AddClientPreferencesRequest | 
    try {
      Object result = apiInstance.addClientPreferences(contentType, accept, orderFormId, addClientPreferencesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartAttachmentsApi#addClientPreferences");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *https://vtex.local*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CartAttachmentsApi* | [**addClientPreferences**](docs/CartAttachmentsApi.md#addClientPreferences) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/clientPreferencesData | Add client preferences
*CartAttachmentsApi* | [**addClientProfile**](docs/CartAttachmentsApi.md#addClientProfile) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/clientProfileData | Add client profile
*CartAttachmentsApi* | [**addMarketingData**](docs/CartAttachmentsApi.md#addMarketingData) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/marketingData | Add marketing data
*CartAttachmentsApi* | [**addMerchantContextData**](docs/CartAttachmentsApi.md#addMerchantContextData) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/merchantContextData | Add merchant context data
*CartAttachmentsApi* | [**addPaymentData**](docs/CartAttachmentsApi.md#addPaymentData) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/paymentData | Add payment data
*CartAttachmentsApi* | [**addShippingAddress**](docs/CartAttachmentsApi.md#addShippingAddress) | **POST** /api/checkout/pub/orderForm/{orderFormId}/attachments/shippingData | Add shipping address and select delivery option
*CartAttachmentsApi* | [**getClientProfileByEmail**](docs/CartAttachmentsApi.md#getClientProfileByEmail) | **GET** /api/checkout/pub/profiles | Get client profile by email
*ConfigurationApi* | [**clearorderFormMessages**](docs/ConfigurationApi.md#clearorderFormMessages) | **POST** /api/checkout/pub/orderForm/{orderFormId}/messages/clear | Clear orderForm messages
*ConfigurationApi* | [**getWindowToChangeSeller**](docs/ConfigurationApi.md#getWindowToChangeSeller) | **GET** /api/checkout/pvt/configuration/window-to-change-seller | Get window to change seller
*ConfigurationApi* | [**getorderFormconfiguration**](docs/ConfigurationApi.md#getorderFormconfiguration) | **GET** /api/checkout/pvt/configuration/orderForm | Get orderForm configuration
*ConfigurationApi* | [**updateWindowToChangeSeller**](docs/ConfigurationApi.md#updateWindowToChangeSeller) | **POST** /api/checkout/pvt/configuration/window-to-change-seller | Update window to change seller
*ConfigurationApi* | [**updateorderFormconfiguration**](docs/ConfigurationApi.md#updateorderFormconfiguration) | **POST** /api/checkout/pvt/configuration/orderForm | Update orderForm configuration
*CustomDataApi* | [**removesinglecustomfieldvalue**](docs/CustomDataApi.md#removesinglecustomfieldvalue) | **DELETE** /api/checkout/pub/orderForm/{orderFormId}/customData/{appId}/{appFieldName} | Remove single custom field value
*CustomDataApi* | [**setMultipleCustomFieldValues**](docs/CustomDataApi.md#setMultipleCustomFieldValues) | **PUT** /api/checkout/pub/orderForm/{orderFormId}/customData/{appId} | Set multiple custom field values
*CustomDataApi* | [**setSingleCustomFieldValue**](docs/CustomDataApi.md#setSingleCustomFieldValue) | **PUT** /api/checkout/pub/orderForm/{orderFormId}/customData/{appId}/{appFieldName} | Set single custom field value
*FulfillmentApi* | [**getAddressByPostalCode**](docs/FulfillmentApi.md#getAddressByPostalCode) | **GET** /api/checkout/pub/postal-code/{countryCode}/{postalCode} | Get address by postal code
*FulfillmentApi* | [**listPickupPpointsByLocation**](docs/FulfillmentApi.md#listPickupPpointsByLocation) | **GET** /api/checkout/pub/pickup-points | List pickup points by location
*OrderPlacementApi* | [**placeOrder**](docs/OrderPlacementApi.md#placeOrder) | **PUT** /api/checkout/pub/orders | Place order
*OrderPlacementApi* | [**placeOrderFromExistingOrderForm**](docs/OrderPlacementApi.md#placeOrderFromExistingOrderForm) | **POST** /api/checkout/pub/orderForm/{orderFormId}/transaction | Place order from an existing cart
*OrderPlacementApi* | [**processOrder**](docs/OrderPlacementApi.md#processOrder) | **POST** /api/checkout/pub/gatewayCallback/{orderGroup} | Process order
*RegionApi* | [**getSellersByRegion**](docs/RegionApi.md#getSellersByRegion) | **GET** /api/checkout/pub/regions/{regionId} | Get sellers by region or address
*ShoppingCartApi* | [**addCoupons**](docs/ShoppingCartApi.md#addCoupons) | **POST** /api/checkout/pub/orderForm/{orderFormId}/coupons | Add coupons to the cart
*ShoppingCartApi* | [**cartSimulation**](docs/ShoppingCartApi.md#cartSimulation) | **POST** /api/checkout/pub/orderForms/simulation | Cart simulation
*ShoppingCartApi* | [**createANewCart**](docs/ShoppingCartApi.md#createANewCart) | **GET** /api/checkout/pub/orderForm | Get current or create a new cart
*ShoppingCartApi* | [**getCartInformationById**](docs/ShoppingCartApi.md#getCartInformationById) | **GET** /api/checkout/pub/orderForm/{orderFormId} | Get cart information by ID
*ShoppingCartApi* | [**getCartInstallments**](docs/ShoppingCartApi.md#getCartInstallments) | **GET** /api/checkout/pub/orderForm/{orderFormId}/installments | Cart installments
*ShoppingCartApi* | [**ignoreProfileData**](docs/ShoppingCartApi.md#ignoreProfileData) | **PATCH** /api/checkout/pub/orderForm/{orderFormId}/profile | Ignore profile data
*ShoppingCartApi* | [**items**](docs/ShoppingCartApi.md#items) | **POST** /api/checkout/pub/orderForm/{orderFormId}/items | Add cart items
*ShoppingCartApi* | [**itemsUpdate**](docs/ShoppingCartApi.md#itemsUpdate) | **POST** /api/checkout/pub/orderForm/{orderFormId}/items/update | Update cart items
*ShoppingCartApi* | [**priceChange**](docs/ShoppingCartApi.md#priceChange) | **PUT** /api/checkout/pub/orderForm/{orderFormId}/items/{itemIndex}/price | Change price
*ShoppingCartApi* | [**removeAllItems**](docs/ShoppingCartApi.md#removeAllItems) | **POST** /api/checkout/pub/orderForm/{orderFormId}/items/removeAll | Remove all items
*ShoppingCartApi* | [**removeallpersonaldata**](docs/ShoppingCartApi.md#removeallpersonaldata) | **GET** /checkout/changeToAnonymousUser/{orderFormId} | Remove all personal data


## Documentation for Models

 - [AddClientPreferencesRequest](docs/AddClientPreferencesRequest.md)
 - [AddClientProfileRequest](docs/AddClientProfileRequest.md)
 - [AddCoupons200Response](docs/AddCoupons200Response.md)
 - [AddCoupons200ResponseAvailableAddressesInner](docs/AddCoupons200ResponseAvailableAddressesInner.md)
 - [AddCoupons200ResponseClientPreferencesData](docs/AddCoupons200ResponseClientPreferencesData.md)
 - [AddCoupons200ResponseClientProfileData](docs/AddCoupons200ResponseClientProfileData.md)
 - [AddCoupons200ResponseItemMetadata](docs/AddCoupons200ResponseItemMetadata.md)
 - [AddCoupons200ResponseItemMetadataItemsInner](docs/AddCoupons200ResponseItemMetadataItemsInner.md)
 - [AddCoupons200ResponseItemsInner](docs/AddCoupons200ResponseItemsInner.md)
 - [AddCoupons200ResponseItemsInnerAdditionalInfo](docs/AddCoupons200ResponseItemsInnerAdditionalInfo.md)
 - [AddCoupons200ResponseItemsInnerBundleItemsInner](docs/AddCoupons200ResponseItemsInnerBundleItemsInner.md)
 - [AddCoupons200ResponseItemsInnerPriceDefinition](docs/AddCoupons200ResponseItemsInnerPriceDefinition.md)
 - [AddCoupons200ResponseItemsInnerPriceDefinitionSellingPricesInner](docs/AddCoupons200ResponseItemsInnerPriceDefinitionSellingPricesInner.md)
 - [AddCoupons200ResponseItemsInnerPriceTagsInner](docs/AddCoupons200ResponseItemsInnerPriceTagsInner.md)
 - [AddCoupons200ResponseItemsInnerProductCategories](docs/AddCoupons200ResponseItemsInnerProductCategories.md)
 - [AddCoupons200ResponseItemsOrdination](docs/AddCoupons200ResponseItemsOrdination.md)
 - [AddCoupons200ResponseMarketingData](docs/AddCoupons200ResponseMarketingData.md)
 - [AddCoupons200ResponsePaymentData](docs/AddCoupons200ResponsePaymentData.md)
 - [AddCoupons200ResponsePaymentDataGiftCardsInner](docs/AddCoupons200ResponsePaymentDataGiftCardsInner.md)
 - [AddCoupons200ResponsePaymentDataTransactionsInner](docs/AddCoupons200ResponsePaymentDataTransactionsInner.md)
 - [AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner](docs/AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner.md)
 - [AddCoupons200ResponseRatesAndBenefitsData](docs/AddCoupons200ResponseRatesAndBenefitsData.md)
 - [AddCoupons200ResponseSellersInner](docs/AddCoupons200ResponseSellersInner.md)
 - [AddCoupons200ResponseShippingData](docs/AddCoupons200ResponseShippingData.md)
 - [AddCoupons200ResponseShippingDataAddress](docs/AddCoupons200ResponseShippingDataAddress.md)
 - [AddCoupons200ResponseShippingDataAvailableAddressesInner](docs/AddCoupons200ResponseShippingDataAvailableAddressesInner.md)
 - [AddCoupons200ResponseShippingDataLogisticsInfoInner](docs/AddCoupons200ResponseShippingDataLogisticsInfoInner.md)
 - [AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner](docs/AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner.md)
 - [AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInner](docs/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInner.md)
 - [AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner](docs/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner.md)
 - [AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo](docs/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo.md)
 - [AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress](docs/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress.md)
 - [AddCouponsRequest](docs/AddCouponsRequest.md)
 - [AddMarketingDataRequest](docs/AddMarketingDataRequest.md)
 - [AddMerchantContextData200Response](docs/AddMerchantContextData200Response.md)
 - [AddMerchantContextDataRequest](docs/AddMerchantContextDataRequest.md)
 - [AddMerchantContextDataRequestSalesAssociateData](docs/AddMerchantContextDataRequestSalesAssociateData.md)
 - [AddPaymentDataRequest](docs/AddPaymentDataRequest.md)
 - [AddPaymentDataRequestPaymentsInner](docs/AddPaymentDataRequestPaymentsInner.md)
 - [AddShippingAddressRequest](docs/AddShippingAddressRequest.md)
 - [AddShippingAddressRequestLogisticsInfoInner](docs/AddShippingAddressRequestLogisticsInfoInner.md)
 - [AddShippingAddressRequestSelectedAddressesInner](docs/AddShippingAddressRequestSelectedAddressesInner.md)
 - [CartSimulation200Response](docs/CartSimulation200Response.md)
 - [CartSimulation200ResponseItemsInner](docs/CartSimulation200ResponseItemsInner.md)
 - [CartSimulation200ResponseItemsInnerPriceTagsInner](docs/CartSimulation200ResponseItemsInnerPriceTagsInner.md)
 - [CartSimulation200ResponseLogisticsInfoInner](docs/CartSimulation200ResponseLogisticsInfoInner.md)
 - [CartSimulation200ResponseLogisticsInfoInnerItemMetadata](docs/CartSimulation200ResponseLogisticsInfoInnerItemMetadata.md)
 - [CartSimulation200ResponseLogisticsInfoInnerItemMetadataItemsInner](docs/CartSimulation200ResponseLogisticsInfoInnerItemMetadataItemsInner.md)
 - [CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions](docs/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions.md)
 - [CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner](docs/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner.md)
 - [CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner](docs/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner.md)
 - [CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows](docs/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows.md)
 - [CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow](docs/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow.md)
 - [CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo](docs/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo.md)
 - [CartSimulation200ResponseLogisticsInfoInnerTotalsInner](docs/CartSimulation200ResponseLogisticsInfoInnerTotalsInner.md)
 - [CartSimulation200ResponsePaymentData](docs/CartSimulation200ResponsePaymentData.md)
 - [CartSimulation200ResponsePaymentDataPaymentSystemsInner](docs/CartSimulation200ResponsePaymentDataPaymentSystemsInner.md)
 - [CartSimulation200ResponseRatesAndBenefitsData](docs/CartSimulation200ResponseRatesAndBenefitsData.md)
 - [CartSimulationRequest](docs/CartSimulationRequest.md)
 - [CartSimulationRequestItemsInner](docs/CartSimulationRequestItemsInner.md)
 - [ClearorderFormMessages200Response](docs/ClearorderFormMessages200Response.md)
 - [ClearorderFormMessages200ResponseMarketingData](docs/ClearorderFormMessages200ResponseMarketingData.md)
 - [GetClientProfileByEmail200Response](docs/GetClientProfileByEmail200Response.md)
 - [GetClientProfileByEmail200ResponseUserProfile](docs/GetClientProfileByEmail200ResponseUserProfile.md)
 - [GetSellersByRegion200Response](docs/GetSellersByRegion200Response.md)
 - [IgnoreProfileDataRequest](docs/IgnoreProfileDataRequest.md)
 - [Item](docs/Item.md)
 - [Items200Response](docs/Items200Response.md)
 - [Items200ResponseClientPreferencesData](docs/Items200ResponseClientPreferencesData.md)
 - [Items200ResponseItemsInner](docs/Items200ResponseItemsInner.md)
 - [Items200ResponseMarketingData](docs/Items200ResponseMarketingData.md)
 - [ItemsRequest](docs/ItemsRequest.md)
 - [ItemsRequestOrderItemsInner](docs/ItemsRequestOrderItemsInner.md)
 - [ItemsUpdate200Response](docs/ItemsUpdate200Response.md)
 - [ItemsUpdate200ResponseAvailableAddressesInner](docs/ItemsUpdate200ResponseAvailableAddressesInner.md)
 - [ItemsUpdate200ResponseItemsOrdination](docs/ItemsUpdate200ResponseItemsOrdination.md)
 - [ItemsUpdate200ResponseShippingData](docs/ItemsUpdate200ResponseShippingData.md)
 - [ItemsUpdate200ResponseShippingDataAddress](docs/ItemsUpdate200ResponseShippingDataAddress.md)
 - [ItemsUpdate200ResponseShippingDataAvailableAddressesInner](docs/ItemsUpdate200ResponseShippingDataAvailableAddressesInner.md)
 - [ItemsUpdate200ResponseShippingDataLogisticsInfoInner](docs/ItemsUpdate200ResponseShippingDataLogisticsInfoInner.md)
 - [ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner](docs/ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner.md)
 - [ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo](docs/ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo.md)
 - [ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress](docs/ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress.md)
 - [ItemsUpdateRequest](docs/ItemsUpdateRequest.md)
 - [ItemsUpdateRequestOrderItemsInner](docs/ItemsUpdateRequestOrderItemsInner.md)
 - [OrderFormSimulationRequest](docs/OrderFormSimulationRequest.md)
 - [PaymentConfiguration](docs/PaymentConfiguration.md)
 - [PlaceOrder200Response](docs/PlaceOrder200Response.md)
 - [PlaceOrder200ResponseOrdersInner](docs/PlaceOrder200ResponseOrdersInner.md)
 - [PlaceOrder200ResponseOrdersInnerItemsInner](docs/PlaceOrder200ResponseOrdersInnerItemsInner.md)
 - [PlaceOrder200ResponseTransactionData](docs/PlaceOrder200ResponseTransactionData.md)
 - [PlaceOrder200ResponseTransactionDataMerchantTransactionsInner](docs/PlaceOrder200ResponseTransactionDataMerchantTransactionsInner.md)
 - [PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner](docs/PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner.md)
 - [PlaceOrderFromExistingOrderFormRequest](docs/PlaceOrderFromExistingOrderFormRequest.md)
 - [PlaceOrderRequest](docs/PlaceOrderRequest.md)
 - [PlaceOrderRequestClientProfileData](docs/PlaceOrderRequestClientProfileData.md)
 - [PlaceOrderRequestItemsInner](docs/PlaceOrderRequestItemsInner.md)
 - [PlaceOrderRequestItemsInnerBundleItemsInner](docs/PlaceOrderRequestItemsInnerBundleItemsInner.md)
 - [PlaceOrderRequestItemsInnerItemAttachment](docs/PlaceOrderRequestItemsInnerItemAttachment.md)
 - [PlaceOrderRequestItemsInnerPriceTagsInner](docs/PlaceOrderRequestItemsInnerPriceTagsInner.md)
 - [PlaceOrderRequestMarketingData](docs/PlaceOrderRequestMarketingData.md)
 - [PlaceOrderRequestPaymentData](docs/PlaceOrderRequestPaymentData.md)
 - [PlaceOrderRequestPaymentDataGiftCardsInner](docs/PlaceOrderRequestPaymentDataGiftCardsInner.md)
 - [PlaceOrderRequestPaymentDataPaymentSystemsInner](docs/PlaceOrderRequestPaymentDataPaymentSystemsInner.md)
 - [PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator](docs/PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator.md)
 - [PlaceOrderRequestPaymentDataPaymentsInner](docs/PlaceOrderRequestPaymentDataPaymentsInner.md)
 - [PlaceOrderRequestShippingData](docs/PlaceOrderRequestShippingData.md)
 - [PlaceOrderRequestShippingDataAddress](docs/PlaceOrderRequestShippingDataAddress.md)
 - [PlaceOrderRequestShippingDataLogisticsInfoInner](docs/PlaceOrderRequestShippingDataLogisticsInfoInner.md)
 - [PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow](docs/PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow.md)
 - [PriceChangeRequest](docs/PriceChangeRequest.md)
 - [ProcessOrder500Response](docs/ProcessOrder500Response.md)
 - [ProcessOrder500ResponseError](docs/ProcessOrder500ResponseError.md)
 - [SetsinglecustomfieldvalueRequest](docs/SetsinglecustomfieldvalueRequest.md)
 - [UpdateorderFormconfigurationRequest](docs/UpdateorderFormconfigurationRequest.md)
 - [UpdateorderFormconfigurationRequestAppsInner](docs/UpdateorderFormconfigurationRequestAppsInner.md)
 - [UpdateorderFormconfigurationRequestTaxConfiguration](docs/UpdateorderFormconfigurationRequestTaxConfiguration.md)
 - [WaitingTime](docs/WaitingTime.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="appKey"></a>
### appKey

- **Type**: API key
- **API key parameter name**: X-VTEX-API-AppKey
- **Location**: HTTP header

<a id="appToken"></a>
### appToken

- **Type**: API key
- **API key parameter name**: X-VTEX-API-AppToken
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



