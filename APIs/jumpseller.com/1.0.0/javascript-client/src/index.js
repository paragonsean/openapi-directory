/**
 * Jumpseller API
 * # Endpoint Structure  All URLs are in the format:   ```text https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken   ```  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. <br/><br/> ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls. <br/><br/> ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. <br/><br/> ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX ```  In curl, you can invoque that URL with:    ```text curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" ```  To create a product, you will include the JSON data and specify the MIME Type:    ```text curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  and to update the product identified with 123:    ```text curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  or delete it:    ```text curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ``` <br/><br/> ***  # PHP Examples  Create a new Product (POST method)  ```php $url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX; $ch = curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');  $result = curl_exec($ch); print_r($result); curl_close($ch); ``` <br/><br/> ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \"created_at\").   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**. <br/><br/> ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  ```ruby tries = 0; max_tries = 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries += 1 rescue   unless tries >= max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end ```  Finally, you can review the Response Headers of each request:  ```text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval ```   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted. <br/><br/> ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.  ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100 ``` <br/><br/> ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. <br/><br/> *** <br/><br/> 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import AddProductCustomField from './model/AddProductCustomField';
import AddProductCustomFieldFields from './model/AddProductCustomFieldFields';
import App from './model/App';
import AppFields from './model/AppFields';
import Attachment from './model/Attachment';
import AttachmentEdit from './model/AttachmentEdit';
import AttachmentEditFields from './model/AttachmentEditFields';
import AttachmentFields from './model/AttachmentFields';
import BadParams from './model/BadParams';
import BestSold from './model/BestSold';
import BillingAddress from './model/BillingAddress';
import Category from './model/Category';
import CategoryEdit from './model/CategoryEdit';
import CategoryEditFields from './model/CategoryEditFields';
import CategoryFields from './model/CategoryFields';
import CheckoutCustomField from './model/CheckoutCustomField';
import CheckoutCustomFieldEdit from './model/CheckoutCustomFieldEdit';
import CheckoutCustomFieldEditFields from './model/CheckoutCustomFieldEditFields';
import CheckoutCustomFieldFields from './model/CheckoutCustomFieldFields';
import Count from './model/Count';
import Country from './model/Country';
import CountryOrders from './model/CountryOrders';
import CustomField from './model/CustomField';
import CustomFieldEdit from './model/CustomFieldEdit';
import CustomFieldEditFields from './model/CustomFieldEditFields';
import CustomFieldFields from './model/CustomFieldFields';
import CustomFieldSelectOption from './model/CustomFieldSelectOption';
import CustomFieldSelectOptionEdit from './model/CustomFieldSelectOptionEdit';
import CustomFieldSelectOptionEditFields from './model/CustomFieldSelectOptionEditFields';
import CustomFieldSelectOptionFields from './model/CustomFieldSelectOptionFields';
import Customer from './model/Customer';
import CustomerAdditionalField from './model/CustomerAdditionalField';
import CustomerAdditionalFieldEdit from './model/CustomerAdditionalFieldEdit';
import CustomerAdditionalFieldEditFields from './model/CustomerAdditionalFieldEditFields';
import CustomerAdditionalFieldFields from './model/CustomerAdditionalFieldFields';
import CustomerCategory from './model/CustomerCategory';
import CustomerCategoryEdit from './model/CustomerCategoryEdit';
import CustomerCategoryEditFields from './model/CustomerCategoryEditFields';
import CustomerCategoryFields from './model/CustomerCategoryFields';
import CustomerFields from './model/CustomerFields';
import CustomerFieldsWithBillingAddressAndShippingAddressFields from './model/CustomerFieldsWithBillingAddressAndShippingAddressFields';
import CustomerFieldsWithPassword from './model/CustomerFieldsWithPassword';
import CustomerFieldsWithPasswordNoID from './model/CustomerFieldsWithPasswordNoID';
import CustomerToCustomerCategory from './model/CustomerToCustomerCategory';
import CustomerWithPassword from './model/CustomerWithPassword';
import CustomerWithPasswordNoID from './model/CustomerWithPasswordNoID';
import CustomersToCustomerCategory from './model/CustomersToCustomerCategory';
import DailyVisits from './model/DailyVisits';
import DigitalProduct from './model/DigitalProduct';
import DigitalProductEdit from './model/DigitalProductEdit';
import DigitalProductEditFields from './model/DigitalProductEditFields';
import DigitalProductFields from './model/DigitalProductFields';
import Fulfillment from './model/Fulfillment';
import FulfillmentCreate from './model/FulfillmentCreate';
import FulfillmentCreateFields from './model/FulfillmentCreateFields';
import FulfillmentEdit from './model/FulfillmentEdit';
import FulfillmentEditFields from './model/FulfillmentEditFields';
import FulfillmentFields from './model/FulfillmentFields';
import Hook from './model/Hook';
import HookEdit from './model/HookEdit';
import HookEditFields from './model/HookEditFields';
import HookFields from './model/HookFields';
import Id from './model/Id';
import Image from './model/Image';
import ImageEdit from './model/ImageEdit';
import ImageEditFields from './model/ImageEditFields';
import ImageFields from './model/ImageFields';
import JSApp from './model/JSApp';
import JSAppEdit from './model/JSAppEdit';
import Language from './model/Language';
import MessageObject from './model/MessageObject';
import NewPartnerStore from './model/NewPartnerStore';
import NewPartnerStoreStore from './model/NewPartnerStoreStore';
import NewVsReturning from './model/NewVsReturning';
import NotFound from './model/NotFound';
import Order from './model/Order';
import OrderAdditionalFields from './model/OrderAdditionalFields';
import OrderBillingAddress from './model/OrderBillingAddress';
import OrderCreate from './model/OrderCreate';
import OrderCreateFields from './model/OrderCreateFields';
import OrderEdit from './model/OrderEdit';
import OrderEditFields from './model/OrderEditFields';
import OrderFields from './model/OrderFields';
import OrderHistory from './model/OrderHistory';
import OrderHistoryEdit from './model/OrderHistoryEdit';
import OrderHistoryEditFields from './model/OrderHistoryEditFields';
import OrderHistoryFields from './model/OrderHistoryFields';
import OrderProduct from './model/OrderProduct';
import OrderProductOrderCreate from './model/OrderProductOrderCreate';
import OrderProductTax from './model/OrderProductTax';
import OrderShippingAddress from './model/OrderShippingAddress';
import OrderShippingTax from './model/OrderShippingTax';
import OrdersData from './model/OrdersData';
import Page from './model/Page';
import PageCategory from './model/PageCategory';
import PageFields from './model/PageFields';
import PageFieldsImage from './model/PageFieldsImage';
import PageModify from './model/PageModify';
import PageModifyFields from './model/PageModifyFields';
import PageTemplate from './model/PageTemplate';
import PartnerError from './model/PartnerError';
import PartnerStoreCode from './model/PartnerStoreCode';
import PartnerStoreCodeStore from './model/PartnerStoreCodeStore';
import PartnerStoreCreate from './model/PartnerStoreCreate';
import PartnerStoreStatus from './model/PartnerStoreStatus';
import PartnerStoreStatusStatus from './model/PartnerStoreStatusStatus';
import PaymentMethod from './model/PaymentMethod';
import PaymentMethodFields from './model/PaymentMethodFields';
import PaymentMethodFreq from './model/PaymentMethodFreq';
import Product from './model/Product';
import ProductCustomField from './model/ProductCustomField';
import ProductCustomFieldFields from './model/ProductCustomFieldFields';
import ProductEdit from './model/ProductEdit';
import ProductEditFields from './model/ProductEditFields';
import ProductFields from './model/ProductFields';
import ProductOption from './model/ProductOption';
import ProductOptionEdit from './model/ProductOptionEdit';
import ProductOptionEditFields from './model/ProductOptionEditFields';
import ProductOptionFields from './model/ProductOptionFields';
import ProductOptionValue from './model/ProductOptionValue';
import ProductOptionValueEdit from './model/ProductOptionValueEdit';
import ProductOptionValueEditFields from './model/ProductOptionValueEditFields';
import ProductOptionValueFields from './model/ProductOptionValueFields';
import ProductOptionVariantEdit from './model/ProductOptionVariantEdit';
import Promotion from './model/Promotion';
import PromotionEdit from './model/PromotionEdit';
import PromotionEditFields from './model/PromotionEditFields';
import PromotionFields from './model/PromotionFields';
import Referrer from './model/Referrer';
import Region from './model/Region';
import RegionOrders from './model/RegionOrders';
import ShippingAddress from './model/ShippingAddress';
import ShippingMethod from './model/ShippingMethod';
import ShippingMethodEdit from './model/ShippingMethodEdit';
import ShippingMethodEditShippingMethod from './model/ShippingMethodEditShippingMethod';
import ShippingMethodFields from './model/ShippingMethodFields';
import ShippingMethodFreq from './model/ShippingMethodFreq';
import ShippingService from './model/ShippingService';
import StatusInvalid from './model/StatusInvalid';
import Store from './model/Store';
import StoreAddress from './model/StoreAddress';
import StoreCheckStatusJsonGet200Response from './model/StoreCheckStatusJsonGet200Response';
import StoreStats from './model/StoreStats';
import StoreStatsConversions from './model/StoreStatsConversions';
import StoreStatsNewVsReturningCustomers from './model/StoreStatsNewVsReturningCustomers';
import StoreStatsOrders from './model/StoreStatsOrders';
import StoreStatsRegionOrders from './model/StoreStatsRegionOrders';
import Tax from './model/Tax';
import TaxEdit from './model/TaxEdit';
import TaxEditFields from './model/TaxEditFields';
import TaxFields from './model/TaxFields';
import TrafficSource from './model/TrafficSource';
import TrafficType from './model/TrafficType';
import Type from './model/Type';
import Variant from './model/Variant';
import VariantEdit from './model/VariantEdit';
import VariantEditFields from './model/VariantEditFields';
import VariantFields from './model/VariantFields';
import AppsApi from './api/AppsApi';
import CategoriesApi from './api/CategoriesApi';
import CheckoutCustomFieldsApi from './api/CheckoutCustomFieldsApi';
import CountriesApi from './api/CountriesApi';
import CustomFieldSelectOptionsApi from './api/CustomFieldSelectOptionsApi';
import CustomFieldsApi from './api/CustomFieldsApi';
import CustomerAdditionalFieldsApi from './api/CustomerAdditionalFieldsApi';
import CustomerCategoriesApi from './api/CustomerCategoriesApi';
import CustomersApi from './api/CustomersApi';
import FulfillmentsApi from './api/FulfillmentsApi';
import HooksApi from './api/HooksApi';
import OrdersApi from './api/OrdersApi';
import PagesApi from './api/PagesApi';
import PartnersApi from './api/PartnersApi';
import PaymentMethodsApi from './api/PaymentMethodsApi';
import ProductAttachmentsApi from './api/ProductAttachmentsApi';
import ProductCustomFieldsApi from './api/ProductCustomFieldsApi';
import ProductDigitalProductsApi from './api/ProductDigitalProductsApi';
import ProductImagesApi from './api/ProductImagesApi';
import ProductOptionValuesApi from './api/ProductOptionValuesApi';
import ProductOptionsApi from './api/ProductOptionsApi';
import ProductVariantsApi from './api/ProductVariantsApi';
import ProductsApi from './api/ProductsApi';
import PromotionsApi from './api/PromotionsApi';
import RegionsApi from './api/RegionsApi';
import ShippingMethodsApi from './api/ShippingMethodsApi';
import StoresApi from './api/StoresApi';
import TaxesApi from './api/TaxesApi';


/**
* # Endpoint Structure  All URLs are in the format:   &#x60;&#x60;&#x60;text https://api.jumpseller.com/v1/path.json?login&#x3D;XXXXXX&amp;authtoken&#x3D;storetoken   &#x60;&#x60;&#x60;  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. &lt;br/&gt;&lt;br/&gt; ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we&#39;ll increase the version number and maintain stable support for the old urls. &lt;br/&gt;&lt;br/&gt; ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. &lt;br/&gt;&lt;br/&gt; ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    &#x60;&#x60;&#x60;text https://api.jumpseller.com/v1/products.json?login&#x3D;XXXXXX&amp;authtoken&#x3D;XXXXX &#x60;&#x60;&#x60;  In curl, you can invoque that URL with:    &#x60;&#x60;&#x60;text curl -X GET \&quot;https://api.jumpseller.com/v1/products.json?login&#x3D;XXXXXX&amp;authtoken&#x3D;XXXXX\&quot; &#x60;&#x60;&#x60;  To create a product, you will include the JSON data and specify the MIME Type:    &#x60;&#x60;&#x60;text curl -X POST -d &#39;{ \&quot;product\&quot; : {\&quot;name\&quot;: \&quot;My new Product!\&quot;, \&quot;price\&quot;: 100} }&#39; \&quot;https://api.jumpseller.com/v1/products.json?login&#x3D;XXXXXX&amp;authtoken&#x3D;XXXXX\&quot; -H \&quot;Content-Type:application/json\&quot; &#x60;&#x60;&#x60;  and to update the product identified with 123:    &#x60;&#x60;&#x60;text curl -X PUT -d &#39;{ \&quot;product\&quot; : {\&quot;name\&quot;: \&quot;My updated Product!\&quot;, \&quot;price\&quot;: 99} }&#39; \&quot;https://api.jumpseller.com/v1/products/123.json?login&#x3D;XXXXXX&amp;authtoken&#x3D;XXXXX\&quot; -H \&quot;Content-Type:application/json\&quot; &#x60;&#x60;&#x60;  or delete it:    &#x60;&#x60;&#x60;text curl -X DELETE \&quot;https://api.jumpseller.com/v1/products/123.json?login&#x3D;XXXXXX&amp;authtoken&#x3D;XXXXX\&quot; -H \&quot;Content-Type:application/json\&quot; &#x60;&#x60;&#x60; &lt;br/&gt;&lt;br/&gt; ***  # PHP Examples  Create a new Product (POST method)  &#x60;&#x60;&#x60;php $url &#x3D; &#39;https://api.jumpseller.com/v1/products.json?login&#x3D;XXXXX&amp;authtoken&#x3D;XXXXX; $ch &#x3D; curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array(&#39;Content-Type: application/json&#39;));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \&quot;POST\&quot;); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, &#39;{ \&quot;product\&quot; : {\&quot;name\&quot;: \&quot;My updated Product!\&quot;, \&quot;price\&quot;: 99} }&#39;);  $result &#x3D; curl_exec($ch); print_r($result); curl_close($ch); &#x60;&#x60;&#x60; &lt;br/&gt;&lt;br/&gt; ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \&quot;created_at\&quot;).   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request&#39;s body content as **\&quot;application/json\&quot;**. &lt;br/&gt;&lt;br/&gt; ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you&#39;ll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  &#x60;&#x60;&#x60;ruby tries &#x3D; 0; max_tries &#x3D; 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries +&#x3D; 1 rescue   unless tries &gt;&#x3D; max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end &#x60;&#x60;&#x60;  Finally, you can review the Response Headers of each request:  &#x60;&#x60;&#x60;text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval &#x60;&#x60;&#x60;   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header &#x60;Jumpseller-BannedByRateLimit-Reset&#x60; informs you the time when will your ban be reseted. &lt;br/&gt;&lt;br/&gt; ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string &#x60;&amp;limit&#x3D;100&#x60;. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings &#x60;&amp;page&#x3D;2&#x60;, &#x60;&amp;page&#x3D;3&#x60; and so on.  &#x60;&#x60;&#x60;text https://api.jumpseller.com/v1/products.json?login&#x3D;XXXXXX&amp;authtoken&#x3D;XXXXX&amp;page&#x3D;3&amp;limit&#x3D;100 &#x60;&#x60;&#x60; &lt;br/&gt;&lt;br/&gt; ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. &lt;br/&gt;&lt;br/&gt; *** &lt;br/&gt;&lt;br/&gt; .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var JumpsellerApi = require('index'); // See note below*.
* var xxxSvc = new JumpsellerApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new JumpsellerApi.Yyy(); // Construct a model instance.
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
* var xxxSvc = new JumpsellerApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new JumpsellerApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.0
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The AddProductCustomField model constructor.
     * @property {module:model/AddProductCustomField}
     */
    AddProductCustomField,

    /**
     * The AddProductCustomFieldFields model constructor.
     * @property {module:model/AddProductCustomFieldFields}
     */
    AddProductCustomFieldFields,

    /**
     * The App model constructor.
     * @property {module:model/App}
     */
    App,

    /**
     * The AppFields model constructor.
     * @property {module:model/AppFields}
     */
    AppFields,

    /**
     * The Attachment model constructor.
     * @property {module:model/Attachment}
     */
    Attachment,

    /**
     * The AttachmentEdit model constructor.
     * @property {module:model/AttachmentEdit}
     */
    AttachmentEdit,

    /**
     * The AttachmentEditFields model constructor.
     * @property {module:model/AttachmentEditFields}
     */
    AttachmentEditFields,

    /**
     * The AttachmentFields model constructor.
     * @property {module:model/AttachmentFields}
     */
    AttachmentFields,

    /**
     * The BadParams model constructor.
     * @property {module:model/BadParams}
     */
    BadParams,

    /**
     * The BestSold model constructor.
     * @property {module:model/BestSold}
     */
    BestSold,

    /**
     * The BillingAddress model constructor.
     * @property {module:model/BillingAddress}
     */
    BillingAddress,

    /**
     * The Category model constructor.
     * @property {module:model/Category}
     */
    Category,

    /**
     * The CategoryEdit model constructor.
     * @property {module:model/CategoryEdit}
     */
    CategoryEdit,

    /**
     * The CategoryEditFields model constructor.
     * @property {module:model/CategoryEditFields}
     */
    CategoryEditFields,

    /**
     * The CategoryFields model constructor.
     * @property {module:model/CategoryFields}
     */
    CategoryFields,

    /**
     * The CheckoutCustomField model constructor.
     * @property {module:model/CheckoutCustomField}
     */
    CheckoutCustomField,

    /**
     * The CheckoutCustomFieldEdit model constructor.
     * @property {module:model/CheckoutCustomFieldEdit}
     */
    CheckoutCustomFieldEdit,

    /**
     * The CheckoutCustomFieldEditFields model constructor.
     * @property {module:model/CheckoutCustomFieldEditFields}
     */
    CheckoutCustomFieldEditFields,

    /**
     * The CheckoutCustomFieldFields model constructor.
     * @property {module:model/CheckoutCustomFieldFields}
     */
    CheckoutCustomFieldFields,

    /**
     * The Count model constructor.
     * @property {module:model/Count}
     */
    Count,

    /**
     * The Country model constructor.
     * @property {module:model/Country}
     */
    Country,

    /**
     * The CountryOrders model constructor.
     * @property {module:model/CountryOrders}
     */
    CountryOrders,

    /**
     * The CustomField model constructor.
     * @property {module:model/CustomField}
     */
    CustomField,

    /**
     * The CustomFieldEdit model constructor.
     * @property {module:model/CustomFieldEdit}
     */
    CustomFieldEdit,

    /**
     * The CustomFieldEditFields model constructor.
     * @property {module:model/CustomFieldEditFields}
     */
    CustomFieldEditFields,

    /**
     * The CustomFieldFields model constructor.
     * @property {module:model/CustomFieldFields}
     */
    CustomFieldFields,

    /**
     * The CustomFieldSelectOption model constructor.
     * @property {module:model/CustomFieldSelectOption}
     */
    CustomFieldSelectOption,

    /**
     * The CustomFieldSelectOptionEdit model constructor.
     * @property {module:model/CustomFieldSelectOptionEdit}
     */
    CustomFieldSelectOptionEdit,

    /**
     * The CustomFieldSelectOptionEditFields model constructor.
     * @property {module:model/CustomFieldSelectOptionEditFields}
     */
    CustomFieldSelectOptionEditFields,

    /**
     * The CustomFieldSelectOptionFields model constructor.
     * @property {module:model/CustomFieldSelectOptionFields}
     */
    CustomFieldSelectOptionFields,

    /**
     * The Customer model constructor.
     * @property {module:model/Customer}
     */
    Customer,

    /**
     * The CustomerAdditionalField model constructor.
     * @property {module:model/CustomerAdditionalField}
     */
    CustomerAdditionalField,

    /**
     * The CustomerAdditionalFieldEdit model constructor.
     * @property {module:model/CustomerAdditionalFieldEdit}
     */
    CustomerAdditionalFieldEdit,

    /**
     * The CustomerAdditionalFieldEditFields model constructor.
     * @property {module:model/CustomerAdditionalFieldEditFields}
     */
    CustomerAdditionalFieldEditFields,

    /**
     * The CustomerAdditionalFieldFields model constructor.
     * @property {module:model/CustomerAdditionalFieldFields}
     */
    CustomerAdditionalFieldFields,

    /**
     * The CustomerCategory model constructor.
     * @property {module:model/CustomerCategory}
     */
    CustomerCategory,

    /**
     * The CustomerCategoryEdit model constructor.
     * @property {module:model/CustomerCategoryEdit}
     */
    CustomerCategoryEdit,

    /**
     * The CustomerCategoryEditFields model constructor.
     * @property {module:model/CustomerCategoryEditFields}
     */
    CustomerCategoryEditFields,

    /**
     * The CustomerCategoryFields model constructor.
     * @property {module:model/CustomerCategoryFields}
     */
    CustomerCategoryFields,

    /**
     * The CustomerFields model constructor.
     * @property {module:model/CustomerFields}
     */
    CustomerFields,

    /**
     * The CustomerFieldsWithBillingAddressAndShippingAddressFields model constructor.
     * @property {module:model/CustomerFieldsWithBillingAddressAndShippingAddressFields}
     */
    CustomerFieldsWithBillingAddressAndShippingAddressFields,

    /**
     * The CustomerFieldsWithPassword model constructor.
     * @property {module:model/CustomerFieldsWithPassword}
     */
    CustomerFieldsWithPassword,

    /**
     * The CustomerFieldsWithPasswordNoID model constructor.
     * @property {module:model/CustomerFieldsWithPasswordNoID}
     */
    CustomerFieldsWithPasswordNoID,

    /**
     * The CustomerToCustomerCategory model constructor.
     * @property {module:model/CustomerToCustomerCategory}
     */
    CustomerToCustomerCategory,

    /**
     * The CustomerWithPassword model constructor.
     * @property {module:model/CustomerWithPassword}
     */
    CustomerWithPassword,

    /**
     * The CustomerWithPasswordNoID model constructor.
     * @property {module:model/CustomerWithPasswordNoID}
     */
    CustomerWithPasswordNoID,

    /**
     * The CustomersToCustomerCategory model constructor.
     * @property {module:model/CustomersToCustomerCategory}
     */
    CustomersToCustomerCategory,

    /**
     * The DailyVisits model constructor.
     * @property {module:model/DailyVisits}
     */
    DailyVisits,

    /**
     * The DigitalProduct model constructor.
     * @property {module:model/DigitalProduct}
     */
    DigitalProduct,

    /**
     * The DigitalProductEdit model constructor.
     * @property {module:model/DigitalProductEdit}
     */
    DigitalProductEdit,

    /**
     * The DigitalProductEditFields model constructor.
     * @property {module:model/DigitalProductEditFields}
     */
    DigitalProductEditFields,

    /**
     * The DigitalProductFields model constructor.
     * @property {module:model/DigitalProductFields}
     */
    DigitalProductFields,

    /**
     * The Fulfillment model constructor.
     * @property {module:model/Fulfillment}
     */
    Fulfillment,

    /**
     * The FulfillmentCreate model constructor.
     * @property {module:model/FulfillmentCreate}
     */
    FulfillmentCreate,

    /**
     * The FulfillmentCreateFields model constructor.
     * @property {module:model/FulfillmentCreateFields}
     */
    FulfillmentCreateFields,

    /**
     * The FulfillmentEdit model constructor.
     * @property {module:model/FulfillmentEdit}
     */
    FulfillmentEdit,

    /**
     * The FulfillmentEditFields model constructor.
     * @property {module:model/FulfillmentEditFields}
     */
    FulfillmentEditFields,

    /**
     * The FulfillmentFields model constructor.
     * @property {module:model/FulfillmentFields}
     */
    FulfillmentFields,

    /**
     * The Hook model constructor.
     * @property {module:model/Hook}
     */
    Hook,

    /**
     * The HookEdit model constructor.
     * @property {module:model/HookEdit}
     */
    HookEdit,

    /**
     * The HookEditFields model constructor.
     * @property {module:model/HookEditFields}
     */
    HookEditFields,

    /**
     * The HookFields model constructor.
     * @property {module:model/HookFields}
     */
    HookFields,

    /**
     * The Id model constructor.
     * @property {module:model/Id}
     */
    Id,

    /**
     * The Image model constructor.
     * @property {module:model/Image}
     */
    Image,

    /**
     * The ImageEdit model constructor.
     * @property {module:model/ImageEdit}
     */
    ImageEdit,

    /**
     * The ImageEditFields model constructor.
     * @property {module:model/ImageEditFields}
     */
    ImageEditFields,

    /**
     * The ImageFields model constructor.
     * @property {module:model/ImageFields}
     */
    ImageFields,

    /**
     * The JSApp model constructor.
     * @property {module:model/JSApp}
     */
    JSApp,

    /**
     * The JSAppEdit model constructor.
     * @property {module:model/JSAppEdit}
     */
    JSAppEdit,

    /**
     * The Language model constructor.
     * @property {module:model/Language}
     */
    Language,

    /**
     * The MessageObject model constructor.
     * @property {module:model/MessageObject}
     */
    MessageObject,

    /**
     * The NewPartnerStore model constructor.
     * @property {module:model/NewPartnerStore}
     */
    NewPartnerStore,

    /**
     * The NewPartnerStoreStore model constructor.
     * @property {module:model/NewPartnerStoreStore}
     */
    NewPartnerStoreStore,

    /**
     * The NewVsReturning model constructor.
     * @property {module:model/NewVsReturning}
     */
    NewVsReturning,

    /**
     * The NotFound model constructor.
     * @property {module:model/NotFound}
     */
    NotFound,

    /**
     * The Order model constructor.
     * @property {module:model/Order}
     */
    Order,

    /**
     * The OrderAdditionalFields model constructor.
     * @property {module:model/OrderAdditionalFields}
     */
    OrderAdditionalFields,

    /**
     * The OrderBillingAddress model constructor.
     * @property {module:model/OrderBillingAddress}
     */
    OrderBillingAddress,

    /**
     * The OrderCreate model constructor.
     * @property {module:model/OrderCreate}
     */
    OrderCreate,

    /**
     * The OrderCreateFields model constructor.
     * @property {module:model/OrderCreateFields}
     */
    OrderCreateFields,

    /**
     * The OrderEdit model constructor.
     * @property {module:model/OrderEdit}
     */
    OrderEdit,

    /**
     * The OrderEditFields model constructor.
     * @property {module:model/OrderEditFields}
     */
    OrderEditFields,

    /**
     * The OrderFields model constructor.
     * @property {module:model/OrderFields}
     */
    OrderFields,

    /**
     * The OrderHistory model constructor.
     * @property {module:model/OrderHistory}
     */
    OrderHistory,

    /**
     * The OrderHistoryEdit model constructor.
     * @property {module:model/OrderHistoryEdit}
     */
    OrderHistoryEdit,

    /**
     * The OrderHistoryEditFields model constructor.
     * @property {module:model/OrderHistoryEditFields}
     */
    OrderHistoryEditFields,

    /**
     * The OrderHistoryFields model constructor.
     * @property {module:model/OrderHistoryFields}
     */
    OrderHistoryFields,

    /**
     * The OrderProduct model constructor.
     * @property {module:model/OrderProduct}
     */
    OrderProduct,

    /**
     * The OrderProductOrderCreate model constructor.
     * @property {module:model/OrderProductOrderCreate}
     */
    OrderProductOrderCreate,

    /**
     * The OrderProductTax model constructor.
     * @property {module:model/OrderProductTax}
     */
    OrderProductTax,

    /**
     * The OrderShippingAddress model constructor.
     * @property {module:model/OrderShippingAddress}
     */
    OrderShippingAddress,

    /**
     * The OrderShippingTax model constructor.
     * @property {module:model/OrderShippingTax}
     */
    OrderShippingTax,

    /**
     * The OrdersData model constructor.
     * @property {module:model/OrdersData}
     */
    OrdersData,

    /**
     * The Page model constructor.
     * @property {module:model/Page}
     */
    Page,

    /**
     * The PageCategory model constructor.
     * @property {module:model/PageCategory}
     */
    PageCategory,

    /**
     * The PageFields model constructor.
     * @property {module:model/PageFields}
     */
    PageFields,

    /**
     * The PageFieldsImage model constructor.
     * @property {module:model/PageFieldsImage}
     */
    PageFieldsImage,

    /**
     * The PageModify model constructor.
     * @property {module:model/PageModify}
     */
    PageModify,

    /**
     * The PageModifyFields model constructor.
     * @property {module:model/PageModifyFields}
     */
    PageModifyFields,

    /**
     * The PageTemplate model constructor.
     * @property {module:model/PageTemplate}
     */
    PageTemplate,

    /**
     * The PartnerError model constructor.
     * @property {module:model/PartnerError}
     */
    PartnerError,

    /**
     * The PartnerStoreCode model constructor.
     * @property {module:model/PartnerStoreCode}
     */
    PartnerStoreCode,

    /**
     * The PartnerStoreCodeStore model constructor.
     * @property {module:model/PartnerStoreCodeStore}
     */
    PartnerStoreCodeStore,

    /**
     * The PartnerStoreCreate model constructor.
     * @property {module:model/PartnerStoreCreate}
     */
    PartnerStoreCreate,

    /**
     * The PartnerStoreStatus model constructor.
     * @property {module:model/PartnerStoreStatus}
     */
    PartnerStoreStatus,

    /**
     * The PartnerStoreStatusStatus model constructor.
     * @property {module:model/PartnerStoreStatusStatus}
     */
    PartnerStoreStatusStatus,

    /**
     * The PaymentMethod model constructor.
     * @property {module:model/PaymentMethod}
     */
    PaymentMethod,

    /**
     * The PaymentMethodFields model constructor.
     * @property {module:model/PaymentMethodFields}
     */
    PaymentMethodFields,

    /**
     * The PaymentMethodFreq model constructor.
     * @property {module:model/PaymentMethodFreq}
     */
    PaymentMethodFreq,

    /**
     * The Product model constructor.
     * @property {module:model/Product}
     */
    Product,

    /**
     * The ProductCustomField model constructor.
     * @property {module:model/ProductCustomField}
     */
    ProductCustomField,

    /**
     * The ProductCustomFieldFields model constructor.
     * @property {module:model/ProductCustomFieldFields}
     */
    ProductCustomFieldFields,

    /**
     * The ProductEdit model constructor.
     * @property {module:model/ProductEdit}
     */
    ProductEdit,

    /**
     * The ProductEditFields model constructor.
     * @property {module:model/ProductEditFields}
     */
    ProductEditFields,

    /**
     * The ProductFields model constructor.
     * @property {module:model/ProductFields}
     */
    ProductFields,

    /**
     * The ProductOption model constructor.
     * @property {module:model/ProductOption}
     */
    ProductOption,

    /**
     * The ProductOptionEdit model constructor.
     * @property {module:model/ProductOptionEdit}
     */
    ProductOptionEdit,

    /**
     * The ProductOptionEditFields model constructor.
     * @property {module:model/ProductOptionEditFields}
     */
    ProductOptionEditFields,

    /**
     * The ProductOptionFields model constructor.
     * @property {module:model/ProductOptionFields}
     */
    ProductOptionFields,

    /**
     * The ProductOptionValue model constructor.
     * @property {module:model/ProductOptionValue}
     */
    ProductOptionValue,

    /**
     * The ProductOptionValueEdit model constructor.
     * @property {module:model/ProductOptionValueEdit}
     */
    ProductOptionValueEdit,

    /**
     * The ProductOptionValueEditFields model constructor.
     * @property {module:model/ProductOptionValueEditFields}
     */
    ProductOptionValueEditFields,

    /**
     * The ProductOptionValueFields model constructor.
     * @property {module:model/ProductOptionValueFields}
     */
    ProductOptionValueFields,

    /**
     * The ProductOptionVariantEdit model constructor.
     * @property {module:model/ProductOptionVariantEdit}
     */
    ProductOptionVariantEdit,

    /**
     * The Promotion model constructor.
     * @property {module:model/Promotion}
     */
    Promotion,

    /**
     * The PromotionEdit model constructor.
     * @property {module:model/PromotionEdit}
     */
    PromotionEdit,

    /**
     * The PromotionEditFields model constructor.
     * @property {module:model/PromotionEditFields}
     */
    PromotionEditFields,

    /**
     * The PromotionFields model constructor.
     * @property {module:model/PromotionFields}
     */
    PromotionFields,

    /**
     * The Referrer model constructor.
     * @property {module:model/Referrer}
     */
    Referrer,

    /**
     * The Region model constructor.
     * @property {module:model/Region}
     */
    Region,

    /**
     * The RegionOrders model constructor.
     * @property {module:model/RegionOrders}
     */
    RegionOrders,

    /**
     * The ShippingAddress model constructor.
     * @property {module:model/ShippingAddress}
     */
    ShippingAddress,

    /**
     * The ShippingMethod model constructor.
     * @property {module:model/ShippingMethod}
     */
    ShippingMethod,

    /**
     * The ShippingMethodEdit model constructor.
     * @property {module:model/ShippingMethodEdit}
     */
    ShippingMethodEdit,

    /**
     * The ShippingMethodEditShippingMethod model constructor.
     * @property {module:model/ShippingMethodEditShippingMethod}
     */
    ShippingMethodEditShippingMethod,

    /**
     * The ShippingMethodFields model constructor.
     * @property {module:model/ShippingMethodFields}
     */
    ShippingMethodFields,

    /**
     * The ShippingMethodFreq model constructor.
     * @property {module:model/ShippingMethodFreq}
     */
    ShippingMethodFreq,

    /**
     * The ShippingService model constructor.
     * @property {module:model/ShippingService}
     */
    ShippingService,

    /**
     * The StatusInvalid model constructor.
     * @property {module:model/StatusInvalid}
     */
    StatusInvalid,

    /**
     * The Store model constructor.
     * @property {module:model/Store}
     */
    Store,

    /**
     * The StoreAddress model constructor.
     * @property {module:model/StoreAddress}
     */
    StoreAddress,

    /**
     * The StoreCheckStatusJsonGet200Response model constructor.
     * @property {module:model/StoreCheckStatusJsonGet200Response}
     */
    StoreCheckStatusJsonGet200Response,

    /**
     * The StoreStats model constructor.
     * @property {module:model/StoreStats}
     */
    StoreStats,

    /**
     * The StoreStatsConversions model constructor.
     * @property {module:model/StoreStatsConversions}
     */
    StoreStatsConversions,

    /**
     * The StoreStatsNewVsReturningCustomers model constructor.
     * @property {module:model/StoreStatsNewVsReturningCustomers}
     */
    StoreStatsNewVsReturningCustomers,

    /**
     * The StoreStatsOrders model constructor.
     * @property {module:model/StoreStatsOrders}
     */
    StoreStatsOrders,

    /**
     * The StoreStatsRegionOrders model constructor.
     * @property {module:model/StoreStatsRegionOrders}
     */
    StoreStatsRegionOrders,

    /**
     * The Tax model constructor.
     * @property {module:model/Tax}
     */
    Tax,

    /**
     * The TaxEdit model constructor.
     * @property {module:model/TaxEdit}
     */
    TaxEdit,

    /**
     * The TaxEditFields model constructor.
     * @property {module:model/TaxEditFields}
     */
    TaxEditFields,

    /**
     * The TaxFields model constructor.
     * @property {module:model/TaxFields}
     */
    TaxFields,

    /**
     * The TrafficSource model constructor.
     * @property {module:model/TrafficSource}
     */
    TrafficSource,

    /**
     * The TrafficType model constructor.
     * @property {module:model/TrafficType}
     */
    TrafficType,

    /**
     * The Type model constructor.
     * @property {module:model/Type}
     */
    Type,

    /**
     * The Variant model constructor.
     * @property {module:model/Variant}
     */
    Variant,

    /**
     * The VariantEdit model constructor.
     * @property {module:model/VariantEdit}
     */
    VariantEdit,

    /**
     * The VariantEditFields model constructor.
     * @property {module:model/VariantEditFields}
     */
    VariantEditFields,

    /**
     * The VariantFields model constructor.
     * @property {module:model/VariantFields}
     */
    VariantFields,

    /**
    * The AppsApi service constructor.
    * @property {module:api/AppsApi}
    */
    AppsApi,

    /**
    * The CategoriesApi service constructor.
    * @property {module:api/CategoriesApi}
    */
    CategoriesApi,

    /**
    * The CheckoutCustomFieldsApi service constructor.
    * @property {module:api/CheckoutCustomFieldsApi}
    */
    CheckoutCustomFieldsApi,

    /**
    * The CountriesApi service constructor.
    * @property {module:api/CountriesApi}
    */
    CountriesApi,

    /**
    * The CustomFieldSelectOptionsApi service constructor.
    * @property {module:api/CustomFieldSelectOptionsApi}
    */
    CustomFieldSelectOptionsApi,

    /**
    * The CustomFieldsApi service constructor.
    * @property {module:api/CustomFieldsApi}
    */
    CustomFieldsApi,

    /**
    * The CustomerAdditionalFieldsApi service constructor.
    * @property {module:api/CustomerAdditionalFieldsApi}
    */
    CustomerAdditionalFieldsApi,

    /**
    * The CustomerCategoriesApi service constructor.
    * @property {module:api/CustomerCategoriesApi}
    */
    CustomerCategoriesApi,

    /**
    * The CustomersApi service constructor.
    * @property {module:api/CustomersApi}
    */
    CustomersApi,

    /**
    * The FulfillmentsApi service constructor.
    * @property {module:api/FulfillmentsApi}
    */
    FulfillmentsApi,

    /**
    * The HooksApi service constructor.
    * @property {module:api/HooksApi}
    */
    HooksApi,

    /**
    * The OrdersApi service constructor.
    * @property {module:api/OrdersApi}
    */
    OrdersApi,

    /**
    * The PagesApi service constructor.
    * @property {module:api/PagesApi}
    */
    PagesApi,

    /**
    * The PartnersApi service constructor.
    * @property {module:api/PartnersApi}
    */
    PartnersApi,

    /**
    * The PaymentMethodsApi service constructor.
    * @property {module:api/PaymentMethodsApi}
    */
    PaymentMethodsApi,

    /**
    * The ProductAttachmentsApi service constructor.
    * @property {module:api/ProductAttachmentsApi}
    */
    ProductAttachmentsApi,

    /**
    * The ProductCustomFieldsApi service constructor.
    * @property {module:api/ProductCustomFieldsApi}
    */
    ProductCustomFieldsApi,

    /**
    * The ProductDigitalProductsApi service constructor.
    * @property {module:api/ProductDigitalProductsApi}
    */
    ProductDigitalProductsApi,

    /**
    * The ProductImagesApi service constructor.
    * @property {module:api/ProductImagesApi}
    */
    ProductImagesApi,

    /**
    * The ProductOptionValuesApi service constructor.
    * @property {module:api/ProductOptionValuesApi}
    */
    ProductOptionValuesApi,

    /**
    * The ProductOptionsApi service constructor.
    * @property {module:api/ProductOptionsApi}
    */
    ProductOptionsApi,

    /**
    * The ProductVariantsApi service constructor.
    * @property {module:api/ProductVariantsApi}
    */
    ProductVariantsApi,

    /**
    * The ProductsApi service constructor.
    * @property {module:api/ProductsApi}
    */
    ProductsApi,

    /**
    * The PromotionsApi service constructor.
    * @property {module:api/PromotionsApi}
    */
    PromotionsApi,

    /**
    * The RegionsApi service constructor.
    * @property {module:api/RegionsApi}
    */
    RegionsApi,

    /**
    * The ShippingMethodsApi service constructor.
    * @property {module:api/ShippingMethodsApi}
    */
    ShippingMethodsApi,

    /**
    * The StoresApi service constructor.
    * @property {module:api/StoresApi}
    */
    StoresApi,

    /**
    * The TaxesApi service constructor.
    * @property {module:api/TaxesApi}
    */
    TaxesApi
};
