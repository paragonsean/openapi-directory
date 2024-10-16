/**
 * Mailsquad
 * MailSquad offers an affordable and super easy way to create, send and track delightful emails.
 *
 * The version of the OpenAPI document: 0.9
 * Contact: support@mailsquad.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Contact from './model/Contact';
import ContactAdd from './model/ContactAdd';
import ContactCustomFieldSchema from './model/ContactCustomFieldSchema';
import ContactList from './model/ContactList';
import ContactListEventCustomization from './model/ContactListEventCustomization';
import ContactListPage from './model/ContactListPage';
import ContactListUpdate from './model/ContactListUpdate';
import ContactPage from './model/ContactPage';
import ContactUpdate from './model/ContactUpdate';
import ContactsGet401ResponseInner from './model/ContactsGet401ResponseInner';
import ContactsGet404ResponseInner from './model/ContactsGet404ResponseInner';
import ContactsGet422ResponseInner from './model/ContactsGet422ResponseInner';
import NewId from './model/NewId';
import SubscriptionRequest from './model/SubscriptionRequest';
import ContactsApi from './api/ContactsApi';
import ListsApi from './api/ListsApi';
import SubscriptionApi from './api/SubscriptionApi';


/**
* MailSquad offers an affordable and super easy way to create, send and track delightful emails..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var Mailsquad = require('index'); // See note below*.
* var xxxSvc = new Mailsquad.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new Mailsquad.Yyy(); // Construct a model instance.
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
* var xxxSvc = new Mailsquad.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new Mailsquad.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 0.9
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Contact model constructor.
     * @property {module:model/Contact}
     */
    Contact,

    /**
     * The ContactAdd model constructor.
     * @property {module:model/ContactAdd}
     */
    ContactAdd,

    /**
     * The ContactCustomFieldSchema model constructor.
     * @property {module:model/ContactCustomFieldSchema}
     */
    ContactCustomFieldSchema,

    /**
     * The ContactList model constructor.
     * @property {module:model/ContactList}
     */
    ContactList,

    /**
     * The ContactListEventCustomization model constructor.
     * @property {module:model/ContactListEventCustomization}
     */
    ContactListEventCustomization,

    /**
     * The ContactListPage model constructor.
     * @property {module:model/ContactListPage}
     */
    ContactListPage,

    /**
     * The ContactListUpdate model constructor.
     * @property {module:model/ContactListUpdate}
     */
    ContactListUpdate,

    /**
     * The ContactPage model constructor.
     * @property {module:model/ContactPage}
     */
    ContactPage,

    /**
     * The ContactUpdate model constructor.
     * @property {module:model/ContactUpdate}
     */
    ContactUpdate,

    /**
     * The ContactsGet401ResponseInner model constructor.
     * @property {module:model/ContactsGet401ResponseInner}
     */
    ContactsGet401ResponseInner,

    /**
     * The ContactsGet404ResponseInner model constructor.
     * @property {module:model/ContactsGet404ResponseInner}
     */
    ContactsGet404ResponseInner,

    /**
     * The ContactsGet422ResponseInner model constructor.
     * @property {module:model/ContactsGet422ResponseInner}
     */
    ContactsGet422ResponseInner,

    /**
     * The NewId model constructor.
     * @property {module:model/NewId}
     */
    NewId,

    /**
     * The SubscriptionRequest model constructor.
     * @property {module:model/SubscriptionRequest}
     */
    SubscriptionRequest,

    /**
    * The ContactsApi service constructor.
    * @property {module:api/ContactsApi}
    */
    ContactsApi,

    /**
    * The ListsApi service constructor.
    * @property {module:api/ListsApi}
    */
    ListsApi,

    /**
    * The SubscriptionApi service constructor.
    * @property {module:api/SubscriptionApi}
    */
    SubscriptionApi
};
