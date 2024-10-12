/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import ConversationsConversationIdOfferPostRequest from './model/ConversationsConversationIdOfferPostRequest';
import ConversationsConversationIdOfferPostRequestOfferItemsInner from './model/ConversationsConversationIdOfferPostRequestOfferItemsInner';
import ConversationsConversationIdOfferPostRequestPrice from './model/ConversationsConversationIdOfferPostRequestPrice';
import ConversationsConversationIdOfferPostRequestShippingPrice from './model/ConversationsConversationIdOfferPostRequestShippingPrice';
import ConversationsIdOfferPostRequest from './model/ConversationsIdOfferPostRequest';
import ListingsListingIdConversationsPostRequest from './model/ListingsListingIdConversationsPostRequest';
import ListingsPostRequest from './model/ListingsPostRequest';
import ListingsPostRequestCategoriesInner from './model/ListingsPostRequestCategoriesInner';
import ListingsPostRequestCondition from './model/ListingsPostRequestCondition';
import ListingsPostRequestLocation from './model/ListingsPostRequestLocation';
import ListingsPostRequestPreorderInfo from './model/ListingsPostRequestPreorderInfo';
import ListingsPostRequestSeller from './model/ListingsPostRequestSeller';
import ListingsPostRequestShipping from './model/ListingsPostRequestShipping';
import ListingsPostRequestShippingRatesInner from './model/ListingsPostRequestShippingRatesInner';
import ListingsPostRequestVideosInner from './model/ListingsPostRequestVideosInner';
import ListingsSlugFlagPostRequest from './model/ListingsSlugFlagPostRequest';
import MyAccountPutRequest from './model/MyAccountPutRequest';
import MyConversationsIdPutRequest from './model/MyConversationsIdPutRequest';
import MyConversationsPostRequest from './model/MyConversationsPostRequest';
import MyFollowsArticlesPostRequest from './model/MyFollowsArticlesPostRequest';
import MyFollowsSearchPostRequest from './model/MyFollowsSearchPostRequest';
import MyListingsSlugStateEndPutRequest from './model/MyListingsSlugStateEndPutRequest';
import MyNegotiationsIdAcceptPostRequest from './model/MyNegotiationsIdAcceptPostRequest';
import MyOrdersSellingIdMarkPickedUpPostRequest from './model/MyOrdersSellingIdMarkPickedUpPostRequest';
import MyOrdersSellingIdShipPostRequest from './model/MyOrdersSellingIdShipPostRequest';
import ProductsReviewsIdPutRequest from './model/ProductsReviewsIdPutRequest';
import ShopPutRequest from './model/ShopPutRequest';
import ShopPutRequestAddress from './model/ShopPutRequestAddress';
import WebhooksRegistrationsPostRequest from './model/WebhooksRegistrationsPostRequest';
import ArticlesApi from './api/ArticlesApi';
import CategoriesApi from './api/CategoriesApi';
import ComparisonShoppingPagesApi from './api/ComparisonShoppingPagesApi';
import ConversationsApi from './api/ConversationsApi';
import CountriesApi from './api/CountriesApi';
import CspsApi from './api/CspsApi';
import CuratedSetsApi from './api/CuratedSetsApi';
import CurrenciesApi from './api/CurrenciesApi';
import FeedbackApi from './api/FeedbackApi';
import HandpickedApi from './api/HandpickedApi';
import ListingConditionsApi from './api/ListingConditionsApi';
import ListingsApi from './api/ListingsApi';
import MyApi from './api/MyApi';
import OrdersApi from './api/OrdersApi';
import PaymentMethodsApi from './api/PaymentMethodsApi';
import PriceguideApi from './api/PriceguideApi';
import ProductsApi from './api/ProductsApi';
import SalesApi from './api/SalesApi';
import ShippingApi from './api/ShippingApi';
import ShopApi from './api/ShopApi';
import ShopsApi from './api/ShopsApi';
import WantsApi from './api/WantsApi';
import WebhooksApi from './api/WebhooksApi';


/**
* reverb.<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var Reverb = require('index'); // See note below*.
* var xxxSvc = new Reverb.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new Reverb.Yyy(); // Construct a model instance.
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
* var xxxSvc = new Reverb.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new Reverb.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 3.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The ConversationsConversationIdOfferPostRequest model constructor.
     * @property {module:model/ConversationsConversationIdOfferPostRequest}
     */
    ConversationsConversationIdOfferPostRequest,

    /**
     * The ConversationsConversationIdOfferPostRequestOfferItemsInner model constructor.
     * @property {module:model/ConversationsConversationIdOfferPostRequestOfferItemsInner}
     */
    ConversationsConversationIdOfferPostRequestOfferItemsInner,

    /**
     * The ConversationsConversationIdOfferPostRequestPrice model constructor.
     * @property {module:model/ConversationsConversationIdOfferPostRequestPrice}
     */
    ConversationsConversationIdOfferPostRequestPrice,

    /**
     * The ConversationsConversationIdOfferPostRequestShippingPrice model constructor.
     * @property {module:model/ConversationsConversationIdOfferPostRequestShippingPrice}
     */
    ConversationsConversationIdOfferPostRequestShippingPrice,

    /**
     * The ConversationsIdOfferPostRequest model constructor.
     * @property {module:model/ConversationsIdOfferPostRequest}
     */
    ConversationsIdOfferPostRequest,

    /**
     * The ListingsListingIdConversationsPostRequest model constructor.
     * @property {module:model/ListingsListingIdConversationsPostRequest}
     */
    ListingsListingIdConversationsPostRequest,

    /**
     * The ListingsPostRequest model constructor.
     * @property {module:model/ListingsPostRequest}
     */
    ListingsPostRequest,

    /**
     * The ListingsPostRequestCategoriesInner model constructor.
     * @property {module:model/ListingsPostRequestCategoriesInner}
     */
    ListingsPostRequestCategoriesInner,

    /**
     * The ListingsPostRequestCondition model constructor.
     * @property {module:model/ListingsPostRequestCondition}
     */
    ListingsPostRequestCondition,

    /**
     * The ListingsPostRequestLocation model constructor.
     * @property {module:model/ListingsPostRequestLocation}
     */
    ListingsPostRequestLocation,

    /**
     * The ListingsPostRequestPreorderInfo model constructor.
     * @property {module:model/ListingsPostRequestPreorderInfo}
     */
    ListingsPostRequestPreorderInfo,

    /**
     * The ListingsPostRequestSeller model constructor.
     * @property {module:model/ListingsPostRequestSeller}
     */
    ListingsPostRequestSeller,

    /**
     * The ListingsPostRequestShipping model constructor.
     * @property {module:model/ListingsPostRequestShipping}
     */
    ListingsPostRequestShipping,

    /**
     * The ListingsPostRequestShippingRatesInner model constructor.
     * @property {module:model/ListingsPostRequestShippingRatesInner}
     */
    ListingsPostRequestShippingRatesInner,

    /**
     * The ListingsPostRequestVideosInner model constructor.
     * @property {module:model/ListingsPostRequestVideosInner}
     */
    ListingsPostRequestVideosInner,

    /**
     * The ListingsSlugFlagPostRequest model constructor.
     * @property {module:model/ListingsSlugFlagPostRequest}
     */
    ListingsSlugFlagPostRequest,

    /**
     * The MyAccountPutRequest model constructor.
     * @property {module:model/MyAccountPutRequest}
     */
    MyAccountPutRequest,

    /**
     * The MyConversationsIdPutRequest model constructor.
     * @property {module:model/MyConversationsIdPutRequest}
     */
    MyConversationsIdPutRequest,

    /**
     * The MyConversationsPostRequest model constructor.
     * @property {module:model/MyConversationsPostRequest}
     */
    MyConversationsPostRequest,

    /**
     * The MyFollowsArticlesPostRequest model constructor.
     * @property {module:model/MyFollowsArticlesPostRequest}
     */
    MyFollowsArticlesPostRequest,

    /**
     * The MyFollowsSearchPostRequest model constructor.
     * @property {module:model/MyFollowsSearchPostRequest}
     */
    MyFollowsSearchPostRequest,

    /**
     * The MyListingsSlugStateEndPutRequest model constructor.
     * @property {module:model/MyListingsSlugStateEndPutRequest}
     */
    MyListingsSlugStateEndPutRequest,

    /**
     * The MyNegotiationsIdAcceptPostRequest model constructor.
     * @property {module:model/MyNegotiationsIdAcceptPostRequest}
     */
    MyNegotiationsIdAcceptPostRequest,

    /**
     * The MyOrdersSellingIdMarkPickedUpPostRequest model constructor.
     * @property {module:model/MyOrdersSellingIdMarkPickedUpPostRequest}
     */
    MyOrdersSellingIdMarkPickedUpPostRequest,

    /**
     * The MyOrdersSellingIdShipPostRequest model constructor.
     * @property {module:model/MyOrdersSellingIdShipPostRequest}
     */
    MyOrdersSellingIdShipPostRequest,

    /**
     * The ProductsReviewsIdPutRequest model constructor.
     * @property {module:model/ProductsReviewsIdPutRequest}
     */
    ProductsReviewsIdPutRequest,

    /**
     * The ShopPutRequest model constructor.
     * @property {module:model/ShopPutRequest}
     */
    ShopPutRequest,

    /**
     * The ShopPutRequestAddress model constructor.
     * @property {module:model/ShopPutRequestAddress}
     */
    ShopPutRequestAddress,

    /**
     * The WebhooksRegistrationsPostRequest model constructor.
     * @property {module:model/WebhooksRegistrationsPostRequest}
     */
    WebhooksRegistrationsPostRequest,

    /**
    * The ArticlesApi service constructor.
    * @property {module:api/ArticlesApi}
    */
    ArticlesApi,

    /**
    * The CategoriesApi service constructor.
    * @property {module:api/CategoriesApi}
    */
    CategoriesApi,

    /**
    * The ComparisonShoppingPagesApi service constructor.
    * @property {module:api/ComparisonShoppingPagesApi}
    */
    ComparisonShoppingPagesApi,

    /**
    * The ConversationsApi service constructor.
    * @property {module:api/ConversationsApi}
    */
    ConversationsApi,

    /**
    * The CountriesApi service constructor.
    * @property {module:api/CountriesApi}
    */
    CountriesApi,

    /**
    * The CspsApi service constructor.
    * @property {module:api/CspsApi}
    */
    CspsApi,

    /**
    * The CuratedSetsApi service constructor.
    * @property {module:api/CuratedSetsApi}
    */
    CuratedSetsApi,

    /**
    * The CurrenciesApi service constructor.
    * @property {module:api/CurrenciesApi}
    */
    CurrenciesApi,

    /**
    * The FeedbackApi service constructor.
    * @property {module:api/FeedbackApi}
    */
    FeedbackApi,

    /**
    * The HandpickedApi service constructor.
    * @property {module:api/HandpickedApi}
    */
    HandpickedApi,

    /**
    * The ListingConditionsApi service constructor.
    * @property {module:api/ListingConditionsApi}
    */
    ListingConditionsApi,

    /**
    * The ListingsApi service constructor.
    * @property {module:api/ListingsApi}
    */
    ListingsApi,

    /**
    * The MyApi service constructor.
    * @property {module:api/MyApi}
    */
    MyApi,

    /**
    * The OrdersApi service constructor.
    * @property {module:api/OrdersApi}
    */
    OrdersApi,

    /**
    * The PaymentMethodsApi service constructor.
    * @property {module:api/PaymentMethodsApi}
    */
    PaymentMethodsApi,

    /**
    * The PriceguideApi service constructor.
    * @property {module:api/PriceguideApi}
    */
    PriceguideApi,

    /**
    * The ProductsApi service constructor.
    * @property {module:api/ProductsApi}
    */
    ProductsApi,

    /**
    * The SalesApi service constructor.
    * @property {module:api/SalesApi}
    */
    SalesApi,

    /**
    * The ShippingApi service constructor.
    * @property {module:api/ShippingApi}
    */
    ShippingApi,

    /**
    * The ShopApi service constructor.
    * @property {module:api/ShopApi}
    */
    ShopApi,

    /**
    * The ShopsApi service constructor.
    * @property {module:api/ShopsApi}
    */
    ShopsApi,

    /**
    * The WantsApi service constructor.
    * @property {module:api/WantsApi}
    */
    WantsApi,

    /**
    * The WebhooksApi service constructor.
    * @property {module:api/WebhooksApi}
    */
    WebhooksApi
};
