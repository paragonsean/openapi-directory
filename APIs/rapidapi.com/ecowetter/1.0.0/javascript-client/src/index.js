/**
 * Historische  Daten
 * Abfrage von Wetterdaten aus der Vergangenheit. Der maximale Abfragezeitraum beträgt 366 Tage (1 Jahr).
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
import DefaultApi from './api/DefaultApi';


/**
* Abfrage von Wetterdaten aus der Vergangenheit. Der maximale Abfragezeitraum beträgt 366 Tage (1 Jahr)..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var HistorischeDaten = require('index'); // See note below*.
* var xxxSvc = new HistorischeDaten.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new HistorischeDaten.Yyy(); // Construct a model instance.
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
* var xxxSvc = new HistorischeDaten.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new HistorischeDaten.Yyy(); // Construct a model instance.
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
    * The DefaultApi service constructor.
    * @property {module:api/DefaultApi}
    */
    DefaultApi
};
