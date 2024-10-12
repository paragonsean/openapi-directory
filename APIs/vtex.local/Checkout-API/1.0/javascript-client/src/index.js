/**
 * Checkout API
 * >ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    >ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    >⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import AddClientPreferencesRequest from './model/AddClientPreferencesRequest';
import AddClientProfileRequest from './model/AddClientProfileRequest';
import AddCoupons200Response from './model/AddCoupons200Response';
import AddCoupons200ResponseAvailableAddressesInner from './model/AddCoupons200ResponseAvailableAddressesInner';
import AddCoupons200ResponseClientPreferencesData from './model/AddCoupons200ResponseClientPreferencesData';
import AddCoupons200ResponseClientProfileData from './model/AddCoupons200ResponseClientProfileData';
import AddCoupons200ResponseItemMetadata from './model/AddCoupons200ResponseItemMetadata';
import AddCoupons200ResponseItemMetadataItemsInner from './model/AddCoupons200ResponseItemMetadataItemsInner';
import AddCoupons200ResponseItemsInner from './model/AddCoupons200ResponseItemsInner';
import AddCoupons200ResponseItemsInnerAdditionalInfo from './model/AddCoupons200ResponseItemsInnerAdditionalInfo';
import AddCoupons200ResponseItemsInnerBundleItemsInner from './model/AddCoupons200ResponseItemsInnerBundleItemsInner';
import AddCoupons200ResponseItemsInnerPriceDefinition from './model/AddCoupons200ResponseItemsInnerPriceDefinition';
import AddCoupons200ResponseItemsInnerPriceDefinitionSellingPricesInner from './model/AddCoupons200ResponseItemsInnerPriceDefinitionSellingPricesInner';
import AddCoupons200ResponseItemsInnerPriceTagsInner from './model/AddCoupons200ResponseItemsInnerPriceTagsInner';
import AddCoupons200ResponseItemsInnerProductCategories from './model/AddCoupons200ResponseItemsInnerProductCategories';
import AddCoupons200ResponseItemsOrdination from './model/AddCoupons200ResponseItemsOrdination';
import AddCoupons200ResponseMarketingData from './model/AddCoupons200ResponseMarketingData';
import AddCoupons200ResponsePaymentData from './model/AddCoupons200ResponsePaymentData';
import AddCoupons200ResponsePaymentDataGiftCardsInner from './model/AddCoupons200ResponsePaymentDataGiftCardsInner';
import AddCoupons200ResponsePaymentDataTransactionsInner from './model/AddCoupons200ResponsePaymentDataTransactionsInner';
import AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner from './model/AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner';
import AddCoupons200ResponseRatesAndBenefitsData from './model/AddCoupons200ResponseRatesAndBenefitsData';
import AddCoupons200ResponseSellersInner from './model/AddCoupons200ResponseSellersInner';
import AddCoupons200ResponseShippingData from './model/AddCoupons200ResponseShippingData';
import AddCoupons200ResponseShippingDataAddress from './model/AddCoupons200ResponseShippingDataAddress';
import AddCoupons200ResponseShippingDataAvailableAddressesInner from './model/AddCoupons200ResponseShippingDataAvailableAddressesInner';
import AddCoupons200ResponseShippingDataLogisticsInfoInner from './model/AddCoupons200ResponseShippingDataLogisticsInfoInner';
import AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner from './model/AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner';
import AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInner from './model/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInner';
import AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner from './model/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner';
import AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo from './model/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo';
import AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress from './model/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress';
import AddCouponsRequest from './model/AddCouponsRequest';
import AddMarketingDataRequest from './model/AddMarketingDataRequest';
import AddMerchantContextData200Response from './model/AddMerchantContextData200Response';
import AddMerchantContextDataRequest from './model/AddMerchantContextDataRequest';
import AddMerchantContextDataRequestSalesAssociateData from './model/AddMerchantContextDataRequestSalesAssociateData';
import AddPaymentDataRequest from './model/AddPaymentDataRequest';
import AddPaymentDataRequestPaymentsInner from './model/AddPaymentDataRequestPaymentsInner';
import AddShippingAddressRequest from './model/AddShippingAddressRequest';
import AddShippingAddressRequestLogisticsInfoInner from './model/AddShippingAddressRequestLogisticsInfoInner';
import AddShippingAddressRequestSelectedAddressesInner from './model/AddShippingAddressRequestSelectedAddressesInner';
import CartSimulation200Response from './model/CartSimulation200Response';
import CartSimulation200ResponseItemsInner from './model/CartSimulation200ResponseItemsInner';
import CartSimulation200ResponseItemsInnerPriceTagsInner from './model/CartSimulation200ResponseItemsInnerPriceTagsInner';
import CartSimulation200ResponseLogisticsInfoInner from './model/CartSimulation200ResponseLogisticsInfoInner';
import CartSimulation200ResponseLogisticsInfoInnerItemMetadata from './model/CartSimulation200ResponseLogisticsInfoInnerItemMetadata';
import CartSimulation200ResponseLogisticsInfoInnerItemMetadataItemsInner from './model/CartSimulation200ResponseLogisticsInfoInnerItemMetadataItemsInner';
import CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions from './model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions';
import CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner from './model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner';
import CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner from './model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner';
import CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows from './model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows';
import CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow from './model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow';
import CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo from './model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo';
import CartSimulation200ResponseLogisticsInfoInnerTotalsInner from './model/CartSimulation200ResponseLogisticsInfoInnerTotalsInner';
import CartSimulation200ResponsePaymentData from './model/CartSimulation200ResponsePaymentData';
import CartSimulation200ResponsePaymentDataPaymentSystemsInner from './model/CartSimulation200ResponsePaymentDataPaymentSystemsInner';
import CartSimulation200ResponseRatesAndBenefitsData from './model/CartSimulation200ResponseRatesAndBenefitsData';
import CartSimulationRequest from './model/CartSimulationRequest';
import CartSimulationRequestItemsInner from './model/CartSimulationRequestItemsInner';
import ClearorderFormMessages200Response from './model/ClearorderFormMessages200Response';
import ClearorderFormMessages200ResponseMarketingData from './model/ClearorderFormMessages200ResponseMarketingData';
import GetClientProfileByEmail200Response from './model/GetClientProfileByEmail200Response';
import GetClientProfileByEmail200ResponseUserProfile from './model/GetClientProfileByEmail200ResponseUserProfile';
import GetSellersByRegion200Response from './model/GetSellersByRegion200Response';
import IgnoreProfileDataRequest from './model/IgnoreProfileDataRequest';
import Item from './model/Item';
import Items200Response from './model/Items200Response';
import Items200ResponseClientPreferencesData from './model/Items200ResponseClientPreferencesData';
import Items200ResponseItemsInner from './model/Items200ResponseItemsInner';
import Items200ResponseMarketingData from './model/Items200ResponseMarketingData';
import ItemsRequest from './model/ItemsRequest';
import ItemsRequestOrderItemsInner from './model/ItemsRequestOrderItemsInner';
import ItemsUpdate200Response from './model/ItemsUpdate200Response';
import ItemsUpdate200ResponseAvailableAddressesInner from './model/ItemsUpdate200ResponseAvailableAddressesInner';
import ItemsUpdate200ResponseItemsOrdination from './model/ItemsUpdate200ResponseItemsOrdination';
import ItemsUpdate200ResponseShippingData from './model/ItemsUpdate200ResponseShippingData';
import ItemsUpdate200ResponseShippingDataAddress from './model/ItemsUpdate200ResponseShippingDataAddress';
import ItemsUpdate200ResponseShippingDataAvailableAddressesInner from './model/ItemsUpdate200ResponseShippingDataAvailableAddressesInner';
import ItemsUpdate200ResponseShippingDataLogisticsInfoInner from './model/ItemsUpdate200ResponseShippingDataLogisticsInfoInner';
import ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner from './model/ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner';
import ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo from './model/ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo';
import ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress from './model/ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress';
import ItemsUpdateRequest from './model/ItemsUpdateRequest';
import ItemsUpdateRequestOrderItemsInner from './model/ItemsUpdateRequestOrderItemsInner';
import OrderFormSimulationRequest from './model/OrderFormSimulationRequest';
import PaymentConfiguration from './model/PaymentConfiguration';
import PlaceOrder200Response from './model/PlaceOrder200Response';
import PlaceOrder200ResponseOrdersInner from './model/PlaceOrder200ResponseOrdersInner';
import PlaceOrder200ResponseOrdersInnerItemsInner from './model/PlaceOrder200ResponseOrdersInnerItemsInner';
import PlaceOrder200ResponseTransactionData from './model/PlaceOrder200ResponseTransactionData';
import PlaceOrder200ResponseTransactionDataMerchantTransactionsInner from './model/PlaceOrder200ResponseTransactionDataMerchantTransactionsInner';
import PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner from './model/PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner';
import PlaceOrderFromExistingOrderFormRequest from './model/PlaceOrderFromExistingOrderFormRequest';
import PlaceOrderRequest from './model/PlaceOrderRequest';
import PlaceOrderRequestClientProfileData from './model/PlaceOrderRequestClientProfileData';
import PlaceOrderRequestItemsInner from './model/PlaceOrderRequestItemsInner';
import PlaceOrderRequestItemsInnerBundleItemsInner from './model/PlaceOrderRequestItemsInnerBundleItemsInner';
import PlaceOrderRequestItemsInnerItemAttachment from './model/PlaceOrderRequestItemsInnerItemAttachment';
import PlaceOrderRequestItemsInnerPriceTagsInner from './model/PlaceOrderRequestItemsInnerPriceTagsInner';
import PlaceOrderRequestMarketingData from './model/PlaceOrderRequestMarketingData';
import PlaceOrderRequestPaymentData from './model/PlaceOrderRequestPaymentData';
import PlaceOrderRequestPaymentDataGiftCardsInner from './model/PlaceOrderRequestPaymentDataGiftCardsInner';
import PlaceOrderRequestPaymentDataPaymentSystemsInner from './model/PlaceOrderRequestPaymentDataPaymentSystemsInner';
import PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator from './model/PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator';
import PlaceOrderRequestPaymentDataPaymentsInner from './model/PlaceOrderRequestPaymentDataPaymentsInner';
import PlaceOrderRequestShippingData from './model/PlaceOrderRequestShippingData';
import PlaceOrderRequestShippingDataAddress from './model/PlaceOrderRequestShippingDataAddress';
import PlaceOrderRequestShippingDataLogisticsInfoInner from './model/PlaceOrderRequestShippingDataLogisticsInfoInner';
import PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow from './model/PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow';
import PriceChangeRequest from './model/PriceChangeRequest';
import ProcessOrder500Response from './model/ProcessOrder500Response';
import ProcessOrder500ResponseError from './model/ProcessOrder500ResponseError';
import SetsinglecustomfieldvalueRequest from './model/SetsinglecustomfieldvalueRequest';
import UpdateorderFormconfigurationRequest from './model/UpdateorderFormconfigurationRequest';
import UpdateorderFormconfigurationRequestAppsInner from './model/UpdateorderFormconfigurationRequestAppsInner';
import UpdateorderFormconfigurationRequestTaxConfiguration from './model/UpdateorderFormconfigurationRequestTaxConfiguration';
import WaitingTime from './model/WaitingTime';
import CartAttachmentsApi from './api/CartAttachmentsApi';
import ConfigurationApi from './api/ConfigurationApi';
import CustomDataApi from './api/CustomDataApi';
import FulfillmentApi from './api/FulfillmentApi';
import OrderPlacementApi from './api/OrderPlacementApi';
import RegionApi from './api/RegionApi';
import ShoppingCartApi from './api/ShoppingCartApi';


/**
* &gt;ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer&#39;s journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    &gt;ℹ️ Data modification operations (&#x60;POST&#x60;, &#x60;PATCH&#x60;, &#x60;PUT&#x60; or &#x60;DELETE&#x60; endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    &gt;⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion).<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var CheckoutApi = require('index'); // See note below*.
* var xxxSvc = new CheckoutApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new CheckoutApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new CheckoutApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new CheckoutApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AddClientPreferencesRequest model constructor.
     * @property {module:model/AddClientPreferencesRequest}
     */
    AddClientPreferencesRequest,

    /**
     * The AddClientProfileRequest model constructor.
     * @property {module:model/AddClientProfileRequest}
     */
    AddClientProfileRequest,

    /**
     * The AddCoupons200Response model constructor.
     * @property {module:model/AddCoupons200Response}
     */
    AddCoupons200Response,

    /**
     * The AddCoupons200ResponseAvailableAddressesInner model constructor.
     * @property {module:model/AddCoupons200ResponseAvailableAddressesInner}
     */
    AddCoupons200ResponseAvailableAddressesInner,

    /**
     * The AddCoupons200ResponseClientPreferencesData model constructor.
     * @property {module:model/AddCoupons200ResponseClientPreferencesData}
     */
    AddCoupons200ResponseClientPreferencesData,

    /**
     * The AddCoupons200ResponseClientProfileData model constructor.
     * @property {module:model/AddCoupons200ResponseClientProfileData}
     */
    AddCoupons200ResponseClientProfileData,

    /**
     * The AddCoupons200ResponseItemMetadata model constructor.
     * @property {module:model/AddCoupons200ResponseItemMetadata}
     */
    AddCoupons200ResponseItemMetadata,

    /**
     * The AddCoupons200ResponseItemMetadataItemsInner model constructor.
     * @property {module:model/AddCoupons200ResponseItemMetadataItemsInner}
     */
    AddCoupons200ResponseItemMetadataItemsInner,

    /**
     * The AddCoupons200ResponseItemsInner model constructor.
     * @property {module:model/AddCoupons200ResponseItemsInner}
     */
    AddCoupons200ResponseItemsInner,

    /**
     * The AddCoupons200ResponseItemsInnerAdditionalInfo model constructor.
     * @property {module:model/AddCoupons200ResponseItemsInnerAdditionalInfo}
     */
    AddCoupons200ResponseItemsInnerAdditionalInfo,

    /**
     * The AddCoupons200ResponseItemsInnerBundleItemsInner model constructor.
     * @property {module:model/AddCoupons200ResponseItemsInnerBundleItemsInner}
     */
    AddCoupons200ResponseItemsInnerBundleItemsInner,

    /**
     * The AddCoupons200ResponseItemsInnerPriceDefinition model constructor.
     * @property {module:model/AddCoupons200ResponseItemsInnerPriceDefinition}
     */
    AddCoupons200ResponseItemsInnerPriceDefinition,

    /**
     * The AddCoupons200ResponseItemsInnerPriceDefinitionSellingPricesInner model constructor.
     * @property {module:model/AddCoupons200ResponseItemsInnerPriceDefinitionSellingPricesInner}
     */
    AddCoupons200ResponseItemsInnerPriceDefinitionSellingPricesInner,

    /**
     * The AddCoupons200ResponseItemsInnerPriceTagsInner model constructor.
     * @property {module:model/AddCoupons200ResponseItemsInnerPriceTagsInner}
     */
    AddCoupons200ResponseItemsInnerPriceTagsInner,

    /**
     * The AddCoupons200ResponseItemsInnerProductCategories model constructor.
     * @property {module:model/AddCoupons200ResponseItemsInnerProductCategories}
     */
    AddCoupons200ResponseItemsInnerProductCategories,

    /**
     * The AddCoupons200ResponseItemsOrdination model constructor.
     * @property {module:model/AddCoupons200ResponseItemsOrdination}
     */
    AddCoupons200ResponseItemsOrdination,

    /**
     * The AddCoupons200ResponseMarketingData model constructor.
     * @property {module:model/AddCoupons200ResponseMarketingData}
     */
    AddCoupons200ResponseMarketingData,

    /**
     * The AddCoupons200ResponsePaymentData model constructor.
     * @property {module:model/AddCoupons200ResponsePaymentData}
     */
    AddCoupons200ResponsePaymentData,

    /**
     * The AddCoupons200ResponsePaymentDataGiftCardsInner model constructor.
     * @property {module:model/AddCoupons200ResponsePaymentDataGiftCardsInner}
     */
    AddCoupons200ResponsePaymentDataGiftCardsInner,

    /**
     * The AddCoupons200ResponsePaymentDataTransactionsInner model constructor.
     * @property {module:model/AddCoupons200ResponsePaymentDataTransactionsInner}
     */
    AddCoupons200ResponsePaymentDataTransactionsInner,

    /**
     * The AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner model constructor.
     * @property {module:model/AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner}
     */
    AddCoupons200ResponsePaymentDataTransactionsInnerPaymentsInner,

    /**
     * The AddCoupons200ResponseRatesAndBenefitsData model constructor.
     * @property {module:model/AddCoupons200ResponseRatesAndBenefitsData}
     */
    AddCoupons200ResponseRatesAndBenefitsData,

    /**
     * The AddCoupons200ResponseSellersInner model constructor.
     * @property {module:model/AddCoupons200ResponseSellersInner}
     */
    AddCoupons200ResponseSellersInner,

    /**
     * The AddCoupons200ResponseShippingData model constructor.
     * @property {module:model/AddCoupons200ResponseShippingData}
     */
    AddCoupons200ResponseShippingData,

    /**
     * The AddCoupons200ResponseShippingDataAddress model constructor.
     * @property {module:model/AddCoupons200ResponseShippingDataAddress}
     */
    AddCoupons200ResponseShippingDataAddress,

    /**
     * The AddCoupons200ResponseShippingDataAvailableAddressesInner model constructor.
     * @property {module:model/AddCoupons200ResponseShippingDataAvailableAddressesInner}
     */
    AddCoupons200ResponseShippingDataAvailableAddressesInner,

    /**
     * The AddCoupons200ResponseShippingDataLogisticsInfoInner model constructor.
     * @property {module:model/AddCoupons200ResponseShippingDataLogisticsInfoInner}
     */
    AddCoupons200ResponseShippingDataLogisticsInfoInner,

    /**
     * The AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner model constructor.
     * @property {module:model/AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner}
     */
    AddCoupons200ResponseShippingDataLogisticsInfoInnerDeliveryChannelsInner,

    /**
     * The AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInner model constructor.
     * @property {module:model/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInner}
     */
    AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInner,

    /**
     * The AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner model constructor.
     * @property {module:model/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner}
     */
    AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerDeliveryIdsInner,

    /**
     * The AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo model constructor.
     * @property {module:model/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo}
     */
    AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo,

    /**
     * The AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress model constructor.
     * @property {module:model/AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress}
     */
    AddCoupons200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress,

    /**
     * The AddCouponsRequest model constructor.
     * @property {module:model/AddCouponsRequest}
     */
    AddCouponsRequest,

    /**
     * The AddMarketingDataRequest model constructor.
     * @property {module:model/AddMarketingDataRequest}
     */
    AddMarketingDataRequest,

    /**
     * The AddMerchantContextData200Response model constructor.
     * @property {module:model/AddMerchantContextData200Response}
     */
    AddMerchantContextData200Response,

    /**
     * The AddMerchantContextDataRequest model constructor.
     * @property {module:model/AddMerchantContextDataRequest}
     */
    AddMerchantContextDataRequest,

    /**
     * The AddMerchantContextDataRequestSalesAssociateData model constructor.
     * @property {module:model/AddMerchantContextDataRequestSalesAssociateData}
     */
    AddMerchantContextDataRequestSalesAssociateData,

    /**
     * The AddPaymentDataRequest model constructor.
     * @property {module:model/AddPaymentDataRequest}
     */
    AddPaymentDataRequest,

    /**
     * The AddPaymentDataRequestPaymentsInner model constructor.
     * @property {module:model/AddPaymentDataRequestPaymentsInner}
     */
    AddPaymentDataRequestPaymentsInner,

    /**
     * The AddShippingAddressRequest model constructor.
     * @property {module:model/AddShippingAddressRequest}
     */
    AddShippingAddressRequest,

    /**
     * The AddShippingAddressRequestLogisticsInfoInner model constructor.
     * @property {module:model/AddShippingAddressRequestLogisticsInfoInner}
     */
    AddShippingAddressRequestLogisticsInfoInner,

    /**
     * The AddShippingAddressRequestSelectedAddressesInner model constructor.
     * @property {module:model/AddShippingAddressRequestSelectedAddressesInner}
     */
    AddShippingAddressRequestSelectedAddressesInner,

    /**
     * The CartSimulation200Response model constructor.
     * @property {module:model/CartSimulation200Response}
     */
    CartSimulation200Response,

    /**
     * The CartSimulation200ResponseItemsInner model constructor.
     * @property {module:model/CartSimulation200ResponseItemsInner}
     */
    CartSimulation200ResponseItemsInner,

    /**
     * The CartSimulation200ResponseItemsInnerPriceTagsInner model constructor.
     * @property {module:model/CartSimulation200ResponseItemsInnerPriceTagsInner}
     */
    CartSimulation200ResponseItemsInnerPriceTagsInner,

    /**
     * The CartSimulation200ResponseLogisticsInfoInner model constructor.
     * @property {module:model/CartSimulation200ResponseLogisticsInfoInner}
     */
    CartSimulation200ResponseLogisticsInfoInner,

    /**
     * The CartSimulation200ResponseLogisticsInfoInnerItemMetadata model constructor.
     * @property {module:model/CartSimulation200ResponseLogisticsInfoInnerItemMetadata}
     */
    CartSimulation200ResponseLogisticsInfoInnerItemMetadata,

    /**
     * The CartSimulation200ResponseLogisticsInfoInnerItemMetadataItemsInner model constructor.
     * @property {module:model/CartSimulation200ResponseLogisticsInfoInnerItemMetadataItemsInner}
     */
    CartSimulation200ResponseLogisticsInfoInnerItemMetadataItemsInner,

    /**
     * The CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions model constructor.
     * @property {module:model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions}
     */
    CartSimulation200ResponseLogisticsInfoInnerPurchaseConditions,

    /**
     * The CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner model constructor.
     * @property {module:model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner}
     */
    CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInner,

    /**
     * The CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner model constructor.
     * @property {module:model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner}
     */
    CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInner,

    /**
     * The CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows model constructor.
     * @property {module:model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows}
     */
    CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerAvailableDeliveryWindows,

    /**
     * The CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow model constructor.
     * @property {module:model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow}
     */
    CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerDeliveryWindow,

    /**
     * The CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo model constructor.
     * @property {module:model/CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo}
     */
    CartSimulation200ResponseLogisticsInfoInnerPurchaseConditionsItemPurchaseConditionsInnerSlasInnerPickupStoreInfo,

    /**
     * The CartSimulation200ResponseLogisticsInfoInnerTotalsInner model constructor.
     * @property {module:model/CartSimulation200ResponseLogisticsInfoInnerTotalsInner}
     */
    CartSimulation200ResponseLogisticsInfoInnerTotalsInner,

    /**
     * The CartSimulation200ResponsePaymentData model constructor.
     * @property {module:model/CartSimulation200ResponsePaymentData}
     */
    CartSimulation200ResponsePaymentData,

    /**
     * The CartSimulation200ResponsePaymentDataPaymentSystemsInner model constructor.
     * @property {module:model/CartSimulation200ResponsePaymentDataPaymentSystemsInner}
     */
    CartSimulation200ResponsePaymentDataPaymentSystemsInner,

    /**
     * The CartSimulation200ResponseRatesAndBenefitsData model constructor.
     * @property {module:model/CartSimulation200ResponseRatesAndBenefitsData}
     */
    CartSimulation200ResponseRatesAndBenefitsData,

    /**
     * The CartSimulationRequest model constructor.
     * @property {module:model/CartSimulationRequest}
     */
    CartSimulationRequest,

    /**
     * The CartSimulationRequestItemsInner model constructor.
     * @property {module:model/CartSimulationRequestItemsInner}
     */
    CartSimulationRequestItemsInner,

    /**
     * The ClearorderFormMessages200Response model constructor.
     * @property {module:model/ClearorderFormMessages200Response}
     */
    ClearorderFormMessages200Response,

    /**
     * The ClearorderFormMessages200ResponseMarketingData model constructor.
     * @property {module:model/ClearorderFormMessages200ResponseMarketingData}
     */
    ClearorderFormMessages200ResponseMarketingData,

    /**
     * The GetClientProfileByEmail200Response model constructor.
     * @property {module:model/GetClientProfileByEmail200Response}
     */
    GetClientProfileByEmail200Response,

    /**
     * The GetClientProfileByEmail200ResponseUserProfile model constructor.
     * @property {module:model/GetClientProfileByEmail200ResponseUserProfile}
     */
    GetClientProfileByEmail200ResponseUserProfile,

    /**
     * The GetSellersByRegion200Response model constructor.
     * @property {module:model/GetSellersByRegion200Response}
     */
    GetSellersByRegion200Response,

    /**
     * The IgnoreProfileDataRequest model constructor.
     * @property {module:model/IgnoreProfileDataRequest}
     */
    IgnoreProfileDataRequest,

    /**
     * The Item model constructor.
     * @property {module:model/Item}
     */
    Item,

    /**
     * The Items200Response model constructor.
     * @property {module:model/Items200Response}
     */
    Items200Response,

    /**
     * The Items200ResponseClientPreferencesData model constructor.
     * @property {module:model/Items200ResponseClientPreferencesData}
     */
    Items200ResponseClientPreferencesData,

    /**
     * The Items200ResponseItemsInner model constructor.
     * @property {module:model/Items200ResponseItemsInner}
     */
    Items200ResponseItemsInner,

    /**
     * The Items200ResponseMarketingData model constructor.
     * @property {module:model/Items200ResponseMarketingData}
     */
    Items200ResponseMarketingData,

    /**
     * The ItemsRequest model constructor.
     * @property {module:model/ItemsRequest}
     */
    ItemsRequest,

    /**
     * The ItemsRequestOrderItemsInner model constructor.
     * @property {module:model/ItemsRequestOrderItemsInner}
     */
    ItemsRequestOrderItemsInner,

    /**
     * The ItemsUpdate200Response model constructor.
     * @property {module:model/ItemsUpdate200Response}
     */
    ItemsUpdate200Response,

    /**
     * The ItemsUpdate200ResponseAvailableAddressesInner model constructor.
     * @property {module:model/ItemsUpdate200ResponseAvailableAddressesInner}
     */
    ItemsUpdate200ResponseAvailableAddressesInner,

    /**
     * The ItemsUpdate200ResponseItemsOrdination model constructor.
     * @property {module:model/ItemsUpdate200ResponseItemsOrdination}
     */
    ItemsUpdate200ResponseItemsOrdination,

    /**
     * The ItemsUpdate200ResponseShippingData model constructor.
     * @property {module:model/ItemsUpdate200ResponseShippingData}
     */
    ItemsUpdate200ResponseShippingData,

    /**
     * The ItemsUpdate200ResponseShippingDataAddress model constructor.
     * @property {module:model/ItemsUpdate200ResponseShippingDataAddress}
     */
    ItemsUpdate200ResponseShippingDataAddress,

    /**
     * The ItemsUpdate200ResponseShippingDataAvailableAddressesInner model constructor.
     * @property {module:model/ItemsUpdate200ResponseShippingDataAvailableAddressesInner}
     */
    ItemsUpdate200ResponseShippingDataAvailableAddressesInner,

    /**
     * The ItemsUpdate200ResponseShippingDataLogisticsInfoInner model constructor.
     * @property {module:model/ItemsUpdate200ResponseShippingDataLogisticsInfoInner}
     */
    ItemsUpdate200ResponseShippingDataLogisticsInfoInner,

    /**
     * The ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner model constructor.
     * @property {module:model/ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner}
     */
    ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInner,

    /**
     * The ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo model constructor.
     * @property {module:model/ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo}
     */
    ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfo,

    /**
     * The ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress model constructor.
     * @property {module:model/ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress}
     */
    ItemsUpdate200ResponseShippingDataLogisticsInfoInnerSlasInnerPickupStoreInfoAddress,

    /**
     * The ItemsUpdateRequest model constructor.
     * @property {module:model/ItemsUpdateRequest}
     */
    ItemsUpdateRequest,

    /**
     * The ItemsUpdateRequestOrderItemsInner model constructor.
     * @property {module:model/ItemsUpdateRequestOrderItemsInner}
     */
    ItemsUpdateRequestOrderItemsInner,

    /**
     * The OrderFormSimulationRequest model constructor.
     * @property {module:model/OrderFormSimulationRequest}
     */
    OrderFormSimulationRequest,

    /**
     * The PaymentConfiguration model constructor.
     * @property {module:model/PaymentConfiguration}
     */
    PaymentConfiguration,

    /**
     * The PlaceOrder200Response model constructor.
     * @property {module:model/PlaceOrder200Response}
     */
    PlaceOrder200Response,

    /**
     * The PlaceOrder200ResponseOrdersInner model constructor.
     * @property {module:model/PlaceOrder200ResponseOrdersInner}
     */
    PlaceOrder200ResponseOrdersInner,

    /**
     * The PlaceOrder200ResponseOrdersInnerItemsInner model constructor.
     * @property {module:model/PlaceOrder200ResponseOrdersInnerItemsInner}
     */
    PlaceOrder200ResponseOrdersInnerItemsInner,

    /**
     * The PlaceOrder200ResponseTransactionData model constructor.
     * @property {module:model/PlaceOrder200ResponseTransactionData}
     */
    PlaceOrder200ResponseTransactionData,

    /**
     * The PlaceOrder200ResponseTransactionDataMerchantTransactionsInner model constructor.
     * @property {module:model/PlaceOrder200ResponseTransactionDataMerchantTransactionsInner}
     */
    PlaceOrder200ResponseTransactionDataMerchantTransactionsInner,

    /**
     * The PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner model constructor.
     * @property {module:model/PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner}
     */
    PlaceOrder200ResponseTransactionDataMerchantTransactionsInnerPaymentsInner,

    /**
     * The PlaceOrderFromExistingOrderFormRequest model constructor.
     * @property {module:model/PlaceOrderFromExistingOrderFormRequest}
     */
    PlaceOrderFromExistingOrderFormRequest,

    /**
     * The PlaceOrderRequest model constructor.
     * @property {module:model/PlaceOrderRequest}
     */
    PlaceOrderRequest,

    /**
     * The PlaceOrderRequestClientProfileData model constructor.
     * @property {module:model/PlaceOrderRequestClientProfileData}
     */
    PlaceOrderRequestClientProfileData,

    /**
     * The PlaceOrderRequestItemsInner model constructor.
     * @property {module:model/PlaceOrderRequestItemsInner}
     */
    PlaceOrderRequestItemsInner,

    /**
     * The PlaceOrderRequestItemsInnerBundleItemsInner model constructor.
     * @property {module:model/PlaceOrderRequestItemsInnerBundleItemsInner}
     */
    PlaceOrderRequestItemsInnerBundleItemsInner,

    /**
     * The PlaceOrderRequestItemsInnerItemAttachment model constructor.
     * @property {module:model/PlaceOrderRequestItemsInnerItemAttachment}
     */
    PlaceOrderRequestItemsInnerItemAttachment,

    /**
     * The PlaceOrderRequestItemsInnerPriceTagsInner model constructor.
     * @property {module:model/PlaceOrderRequestItemsInnerPriceTagsInner}
     */
    PlaceOrderRequestItemsInnerPriceTagsInner,

    /**
     * The PlaceOrderRequestMarketingData model constructor.
     * @property {module:model/PlaceOrderRequestMarketingData}
     */
    PlaceOrderRequestMarketingData,

    /**
     * The PlaceOrderRequestPaymentData model constructor.
     * @property {module:model/PlaceOrderRequestPaymentData}
     */
    PlaceOrderRequestPaymentData,

    /**
     * The PlaceOrderRequestPaymentDataGiftCardsInner model constructor.
     * @property {module:model/PlaceOrderRequestPaymentDataGiftCardsInner}
     */
    PlaceOrderRequestPaymentDataGiftCardsInner,

    /**
     * The PlaceOrderRequestPaymentDataPaymentSystemsInner model constructor.
     * @property {module:model/PlaceOrderRequestPaymentDataPaymentSystemsInner}
     */
    PlaceOrderRequestPaymentDataPaymentSystemsInner,

    /**
     * The PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator model constructor.
     * @property {module:model/PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator}
     */
    PlaceOrderRequestPaymentDataPaymentSystemsInnerValidator,

    /**
     * The PlaceOrderRequestPaymentDataPaymentsInner model constructor.
     * @property {module:model/PlaceOrderRequestPaymentDataPaymentsInner}
     */
    PlaceOrderRequestPaymentDataPaymentsInner,

    /**
     * The PlaceOrderRequestShippingData model constructor.
     * @property {module:model/PlaceOrderRequestShippingData}
     */
    PlaceOrderRequestShippingData,

    /**
     * The PlaceOrderRequestShippingDataAddress model constructor.
     * @property {module:model/PlaceOrderRequestShippingDataAddress}
     */
    PlaceOrderRequestShippingDataAddress,

    /**
     * The PlaceOrderRequestShippingDataLogisticsInfoInner model constructor.
     * @property {module:model/PlaceOrderRequestShippingDataLogisticsInfoInner}
     */
    PlaceOrderRequestShippingDataLogisticsInfoInner,

    /**
     * The PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow model constructor.
     * @property {module:model/PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow}
     */
    PlaceOrderRequestShippingDataLogisticsInfoInnerDeliveryWindow,

    /**
     * The PriceChangeRequest model constructor.
     * @property {module:model/PriceChangeRequest}
     */
    PriceChangeRequest,

    /**
     * The ProcessOrder500Response model constructor.
     * @property {module:model/ProcessOrder500Response}
     */
    ProcessOrder500Response,

    /**
     * The ProcessOrder500ResponseError model constructor.
     * @property {module:model/ProcessOrder500ResponseError}
     */
    ProcessOrder500ResponseError,

    /**
     * The SetsinglecustomfieldvalueRequest model constructor.
     * @property {module:model/SetsinglecustomfieldvalueRequest}
     */
    SetsinglecustomfieldvalueRequest,

    /**
     * The UpdateorderFormconfigurationRequest model constructor.
     * @property {module:model/UpdateorderFormconfigurationRequest}
     */
    UpdateorderFormconfigurationRequest,

    /**
     * The UpdateorderFormconfigurationRequestAppsInner model constructor.
     * @property {module:model/UpdateorderFormconfigurationRequestAppsInner}
     */
    UpdateorderFormconfigurationRequestAppsInner,

    /**
     * The UpdateorderFormconfigurationRequestTaxConfiguration model constructor.
     * @property {module:model/UpdateorderFormconfigurationRequestTaxConfiguration}
     */
    UpdateorderFormconfigurationRequestTaxConfiguration,

    /**
     * The WaitingTime model constructor.
     * @property {module:model/WaitingTime}
     */
    WaitingTime,

    /**
    * The CartAttachmentsApi service constructor.
    * @property {module:api/CartAttachmentsApi}
    */
    CartAttachmentsApi,

    /**
    * The ConfigurationApi service constructor.
    * @property {module:api/ConfigurationApi}
    */
    ConfigurationApi,

    /**
    * The CustomDataApi service constructor.
    * @property {module:api/CustomDataApi}
    */
    CustomDataApi,

    /**
    * The FulfillmentApi service constructor.
    * @property {module:api/FulfillmentApi}
    */
    FulfillmentApi,

    /**
    * The OrderPlacementApi service constructor.
    * @property {module:api/OrderPlacementApi}
    */
    OrderPlacementApi,

    /**
    * The RegionApi service constructor.
    * @property {module:api/RegionApi}
    */
    RegionApi,

    /**
    * The ShoppingCartApi service constructor.
    * @property {module:api/ShoppingCartApi}
    */
    ShoppingCartApi
};
