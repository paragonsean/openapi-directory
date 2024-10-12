/**
 * Flight Inspiration Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. 
 *
 * The version of the OpenAPI document: 1.0.6
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import Defaults from './model/Defaults';
import Dictionaries from './model/Dictionaries';
import Error400 from './model/Error400';
import Error404 from './model/Error404';
import Error500 from './model/Error500';
import FlightDestination from './model/FlightDestination';
import FlightDestinationLinks from './model/FlightDestinationLinks';
import FlightDestinations from './model/FlightDestinations';
import Issue from './model/Issue';
import IssueSource from './model/IssueSource';
import Links from './model/Links';
import LocationValue from './model/LocationValue';
import Meta from './model/Meta';
import Price from './model/Price';
import FlightDestinationsApi from './api/FlightDestinationsApi';


/**
*  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.  Please also be aware that our test environment is based on a subset of the production, to see what is included in test please refer to our **[data collection](https://github.com/amadeus4dev/data-collection)**. .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var FlightInspirationSearch = require('index'); // See note below*.
* var xxxSvc = new FlightInspirationSearch.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new FlightInspirationSearch.Yyy(); // Construct a model instance.
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
* var xxxSvc = new FlightInspirationSearch.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new FlightInspirationSearch.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 1.0.6
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The Defaults model constructor.
     * @property {module:model/Defaults}
     */
    Defaults,

    /**
     * The Dictionaries model constructor.
     * @property {module:model/Dictionaries}
     */
    Dictionaries,

    /**
     * The Error400 model constructor.
     * @property {module:model/Error400}
     */
    Error400,

    /**
     * The Error404 model constructor.
     * @property {module:model/Error404}
     */
    Error404,

    /**
     * The Error500 model constructor.
     * @property {module:model/Error500}
     */
    Error500,

    /**
     * The FlightDestination model constructor.
     * @property {module:model/FlightDestination}
     */
    FlightDestination,

    /**
     * The FlightDestinationLinks model constructor.
     * @property {module:model/FlightDestinationLinks}
     */
    FlightDestinationLinks,

    /**
     * The FlightDestinations model constructor.
     * @property {module:model/FlightDestinations}
     */
    FlightDestinations,

    /**
     * The Issue model constructor.
     * @property {module:model/Issue}
     */
    Issue,

    /**
     * The IssueSource model constructor.
     * @property {module:model/IssueSource}
     */
    IssueSource,

    /**
     * The Links model constructor.
     * @property {module:model/Links}
     */
    Links,

    /**
     * The LocationValue model constructor.
     * @property {module:model/LocationValue}
     */
    LocationValue,

    /**
     * The Meta model constructor.
     * @property {module:model/Meta}
     */
    Meta,

    /**
     * The Price model constructor.
     * @property {module:model/Price}
     */
    Price,

    /**
    * The FlightDestinationsApi service constructor.
    * @property {module:api/FlightDestinationsApi}
    */
    FlightDestinationsApi
};
