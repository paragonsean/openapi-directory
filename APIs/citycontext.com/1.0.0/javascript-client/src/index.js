/**
 * City Context
 * City Context provides a straightforward API to access UK Open Data: crime statistics, schools, demographics and more.
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
import Location from './model/Location';
import PointInfo from './model/PointInfo';
import PointInfoLsoa from './model/PointInfoLsoa';
import PointInfoLsoaPopulation from './model/PointInfoLsoaPopulation';
import PointInfoParksInner from './model/PointInfoParksInner';
import PointInfoSchoolsInner from './model/PointInfoSchoolsInner';
import Usage from './model/Usage';
import CitycontextApi from './api/CitycontextApi';


/**
* City Context provides a straightforward API to access UK Open Data: crime statistics, schools, demographics and more..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var CityContext = require('index'); // See note below*.
* var xxxSvc = new CityContext.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new CityContext.Yyy(); // Construct a model instance.
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
* var xxxSvc = new CityContext.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new CityContext.Yyy(); // Construct a model instance.
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
     * The Location model constructor.
     * @property {module:model/Location}
     */
    Location,

    /**
     * The PointInfo model constructor.
     * @property {module:model/PointInfo}
     */
    PointInfo,

    /**
     * The PointInfoLsoa model constructor.
     * @property {module:model/PointInfoLsoa}
     */
    PointInfoLsoa,

    /**
     * The PointInfoLsoaPopulation model constructor.
     * @property {module:model/PointInfoLsoaPopulation}
     */
    PointInfoLsoaPopulation,

    /**
     * The PointInfoParksInner model constructor.
     * @property {module:model/PointInfoParksInner}
     */
    PointInfoParksInner,

    /**
     * The PointInfoSchoolsInner model constructor.
     * @property {module:model/PointInfoSchoolsInner}
     */
    PointInfoSchoolsInner,

    /**
     * The Usage model constructor.
     * @property {module:model/Usage}
     */
    Usage,

    /**
    * The CitycontextApi service constructor.
    * @property {module:api/CitycontextApi}
    */
    CitycontextApi
};
