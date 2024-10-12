/**
 * groov View Public API
 * #### Revised: 2019-11-21  ### Overview groov View Public API revision 1. 
 *
 * The version of the OpenAPI document: R4.2a
 * Contact: developer@opto22.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import BooleanArrayValue from './model/BooleanArrayValue';
import BooleanValue from './model/BooleanValue';
import DataStoreDevice from './model/DataStoreDevice';
import Device from './model/Device';
import ErrorValue from './model/ErrorValue';
import FloatArrayValue from './model/FloatArrayValue';
import FloatValue from './model/FloatValue';
import GroovInfo from './model/GroovInfo';
import IntegerArrayValue from './model/IntegerArrayValue';
import IntegerValue from './model/IntegerValue';
import StringArrayValue from './model/StringArrayValue';
import StringValue from './model/StringValue';
import TagDefinition from './model/TagDefinition';
import TagReference from './model/TagReference';
import TagValue from './model/TagValue';
import User from './model/User';
import DataStoreApi from './api/DataStoreApi';
import InfoApi from './api/InfoApi';
import LoggingApi from './api/LoggingApi';
import WhoamiApi from './api/WhoamiApi';


/**
* #### Revised: 2019-11-21  ### Overview groov View Public API revision 1. .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var GroovViewPublicApi = require('index'); // See note below*.
* var xxxSvc = new GroovViewPublicApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new GroovViewPublicApi.Yyy(); // Construct a model instance.
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
* var xxxSvc = new GroovViewPublicApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new GroovViewPublicApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version R4.2a
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The BooleanArrayValue model constructor.
     * @property {module:model/BooleanArrayValue}
     */
    BooleanArrayValue,

    /**
     * The BooleanValue model constructor.
     * @property {module:model/BooleanValue}
     */
    BooleanValue,

    /**
     * The DataStoreDevice model constructor.
     * @property {module:model/DataStoreDevice}
     */
    DataStoreDevice,

    /**
     * The Device model constructor.
     * @property {module:model/Device}
     */
    Device,

    /**
     * The ErrorValue model constructor.
     * @property {module:model/ErrorValue}
     */
    ErrorValue,

    /**
     * The FloatArrayValue model constructor.
     * @property {module:model/FloatArrayValue}
     */
    FloatArrayValue,

    /**
     * The FloatValue model constructor.
     * @property {module:model/FloatValue}
     */
    FloatValue,

    /**
     * The GroovInfo model constructor.
     * @property {module:model/GroovInfo}
     */
    GroovInfo,

    /**
     * The IntegerArrayValue model constructor.
     * @property {module:model/IntegerArrayValue}
     */
    IntegerArrayValue,

    /**
     * The IntegerValue model constructor.
     * @property {module:model/IntegerValue}
     */
    IntegerValue,

    /**
     * The StringArrayValue model constructor.
     * @property {module:model/StringArrayValue}
     */
    StringArrayValue,

    /**
     * The StringValue model constructor.
     * @property {module:model/StringValue}
     */
    StringValue,

    /**
     * The TagDefinition model constructor.
     * @property {module:model/TagDefinition}
     */
    TagDefinition,

    /**
     * The TagReference model constructor.
     * @property {module:model/TagReference}
     */
    TagReference,

    /**
     * The TagValue model constructor.
     * @property {module:model/TagValue}
     */
    TagValue,

    /**
     * The User model constructor.
     * @property {module:model/User}
     */
    User,

    /**
    * The DataStoreApi service constructor.
    * @property {module:api/DataStoreApi}
    */
    DataStoreApi,

    /**
    * The InfoApi service constructor.
    * @property {module:api/InfoApi}
    */
    InfoApi,

    /**
    * The LoggingApi service constructor.
    * @property {module:api/LoggingApi}
    */
    LoggingApi,

    /**
    * The WhoamiApi service constructor.
    * @property {module:api/WhoamiApi}
    */
    WhoamiApi
};
