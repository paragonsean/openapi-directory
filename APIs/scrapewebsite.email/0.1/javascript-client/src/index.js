/**
 * Scrape Website Email API
 * ScrapeWebsiteEmail is a service that exposes an api to fetch e-mails from a website.
 *
 * The version of the OpenAPI document: 0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import PingApi from './api/PingApi';
import ScrapeEmailsApi from './api/ScrapeEmailsApi';
import ScrapeStoreLinksApi from './api/ScrapeStoreLinksApi';


/**
* ScrapeWebsiteEmail is a service that exposes an api to fetch e-mails from a website..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var ScrapeWebsiteEmailApi = require('index'); // See note below*.
* var xxxSvc = new ScrapeWebsiteEmailApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new ScrapeWebsiteEmailApi.Yyy(); // Construct a model instance.
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
* var xxxSvc = new ScrapeWebsiteEmailApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new ScrapeWebsiteEmailApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 0.1
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
    * The PingApi service constructor.
    * @property {module:api/PingApi}
    */
    PingApi,

    /**
    * The ScrapeEmailsApi service constructor.
    * @property {module:api/ScrapeEmailsApi}
    */
    ScrapeEmailsApi,

    /**
    * The ScrapeStoreLinksApi service constructor.
    * @property {module:api/ScrapeStoreLinksApi}
    */
    ScrapeStoreLinksApi
};
