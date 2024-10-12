/**
 * Dataflow Kit Web Scraper
 * Render Javascript driven pages, while we internally manage Headless Chrome and proxies for you.   - Build a custom web scraper with our Visual point-and-click toolkit. - Scrape the most popular Search engines result pages (SERP). - Convert web pages to PDF and capture screenshots. *** ### Authentication Dataflow Kit API require you to sign up for an API key in order to use the API.   The API key can be found in the [DFK Dashboard](https://account.dataflowkit.com) after _free registration_.  Pass a secret API Key to all API requests to the server as the `api_key` query parameter.  
 *
 * The version of the OpenAPI document: 1.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Action from './model/Action';
import Click from './model/Click';
import DoubleClick from './model/DoubleClick';
import Execute from './model/Execute';
import Fetchrequest from './model/Fetchrequest';
import Field from './model/Field';
import FieldFiltersInner from './model/FieldFiltersInner';
import FieldFiltersInnerAnyOf from './model/FieldFiltersInnerAnyOf';
import FieldFiltersInnerAnyOf1 from './model/FieldFiltersInnerAnyOf1';
import Getcontent from './model/Getcontent';
import InitialCookie from './model/InitialCookie';
import Input from './model/Input';
import Jsclick from './model/Jsclick';
import LoopTimes from './model/LoopTimes';
import Paginator from './model/Paginator';
import Parserequest from './model/Parserequest';
import Pause from './model/Pause';
import Scroll from './model/Scroll';
import SendKeys from './model/SendKeys';
import Serprequest from './model/Serprequest';
import Submit from './model/Submit';
import Url2pdfrequest from './model/Url2pdfrequest';
import Url2screenshotrequest from './model/Url2screenshotrequest';
import WaitNotVisible from './model/WaitNotVisible';
import WaitVisible from './model/WaitVisible';
import FetchApi from './api/FetchApi';
import ParseApi from './api/ParseApi';
import SerpApi from './api/SerpApi';
import UrlToPdfApi from './api/UrlToPdfApi';
import UrlToScreenshotApi from './api/UrlToScreenshotApi';


/**
* Render Javascript driven pages, while we internally manage Headless Chrome and proxies for you.   - Build a custom web scraper with our Visual point-and-click toolkit. - Scrape the most popular Search engines result pages (SERP). - Convert web pages to PDF and capture screenshots. *** ### Authentication Dataflow Kit API require you to sign up for an API key in order to use the API.   The API key can be found in the [DFK Dashboard](https://account.dataflowkit.com) after _free registration_.  Pass a secret API Key to all API requests to the server as the &#x60;api_key&#x60; query parameter.  .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var DataflowKitWebScraper = require('index'); // See note below*.
* var xxxSvc = new DataflowKitWebScraper.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new DataflowKitWebScraper.Yyy(); // Construct a model instance.
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
* var xxxSvc = new DataflowKitWebScraper.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new DataflowKitWebScraper.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.3
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Action model constructor.
     * @property {module:model/Action}
     */
    Action,

    /**
     * The Click model constructor.
     * @property {module:model/Click}
     */
    Click,

    /**
     * The DoubleClick model constructor.
     * @property {module:model/DoubleClick}
     */
    DoubleClick,

    /**
     * The Execute model constructor.
     * @property {module:model/Execute}
     */
    Execute,

    /**
     * The Fetchrequest model constructor.
     * @property {module:model/Fetchrequest}
     */
    Fetchrequest,

    /**
     * The Field model constructor.
     * @property {module:model/Field}
     */
    Field,

    /**
     * The FieldFiltersInner model constructor.
     * @property {module:model/FieldFiltersInner}
     */
    FieldFiltersInner,

    /**
     * The FieldFiltersInnerAnyOf model constructor.
     * @property {module:model/FieldFiltersInnerAnyOf}
     */
    FieldFiltersInnerAnyOf,

    /**
     * The FieldFiltersInnerAnyOf1 model constructor.
     * @property {module:model/FieldFiltersInnerAnyOf1}
     */
    FieldFiltersInnerAnyOf1,

    /**
     * The Getcontent model constructor.
     * @property {module:model/Getcontent}
     */
    Getcontent,

    /**
     * The InitialCookie model constructor.
     * @property {module:model/InitialCookie}
     */
    InitialCookie,

    /**
     * The Input model constructor.
     * @property {module:model/Input}
     */
    Input,

    /**
     * The Jsclick model constructor.
     * @property {module:model/Jsclick}
     */
    Jsclick,

    /**
     * The LoopTimes model constructor.
     * @property {module:model/LoopTimes}
     */
    LoopTimes,

    /**
     * The Paginator model constructor.
     * @property {module:model/Paginator}
     */
    Paginator,

    /**
     * The Parserequest model constructor.
     * @property {module:model/Parserequest}
     */
    Parserequest,

    /**
     * The Pause model constructor.
     * @property {module:model/Pause}
     */
    Pause,

    /**
     * The Scroll model constructor.
     * @property {module:model/Scroll}
     */
    Scroll,

    /**
     * The SendKeys model constructor.
     * @property {module:model/SendKeys}
     */
    SendKeys,

    /**
     * The Serprequest model constructor.
     * @property {module:model/Serprequest}
     */
    Serprequest,

    /**
     * The Submit model constructor.
     * @property {module:model/Submit}
     */
    Submit,

    /**
     * The Url2pdfrequest model constructor.
     * @property {module:model/Url2pdfrequest}
     */
    Url2pdfrequest,

    /**
     * The Url2screenshotrequest model constructor.
     * @property {module:model/Url2screenshotrequest}
     */
    Url2screenshotrequest,

    /**
     * The WaitNotVisible model constructor.
     * @property {module:model/WaitNotVisible}
     */
    WaitNotVisible,

    /**
     * The WaitVisible model constructor.
     * @property {module:model/WaitVisible}
     */
    WaitVisible,

    /**
    * The FetchApi service constructor.
    * @property {module:api/FetchApi}
    */
    FetchApi,

    /**
    * The ParseApi service constructor.
    * @property {module:api/ParseApi}
    */
    ParseApi,

    /**
    * The SerpApi service constructor.
    * @property {module:api/SerpApi}
    */
    SerpApi,

    /**
    * The UrlToPdfApi service constructor.
    * @property {module:api/UrlToPdfApi}
    */
    UrlToPdfApi,

    /**
    * The UrlToScreenshotApi service constructor.
    * @property {module:api/UrlToScreenshotApi}
    */
    UrlToScreenshotApi
};
