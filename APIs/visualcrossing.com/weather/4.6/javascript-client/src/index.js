/**
 * Visual Crossing Weather API
 * Weather Forecast and Historical Weather Data via RESTful API.
 *
 * The version of the OpenAPI document: 4.6
 * Contact: info@visualcrossing.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import HistoricalWeatherApi from './api/HistoricalWeatherApi';
import TimelineWeatherAPI15DayForecastRequestApi from './api/TimelineWeatherAPI15DayForecastRequestApi';
import TimelineWeatherAPIDateRangeRequestApi from './api/TimelineWeatherAPIDateRangeRequestApi';
import TimelineWeatherAPISingleDateRequestApi from './api/TimelineWeatherAPISingleDateRequestApi';
import WeatherForecastApi from './api/WeatherForecastApi';


/**
* Weather Forecast and Historical Weather Data via RESTful API..<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var VisualCrossingWeatherApi = require('index'); // See note below*.
* var xxxSvc = new VisualCrossingWeatherApi.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new VisualCrossingWeatherApi.Yyy(); // Construct a model instance.
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
* var xxxSvc = new VisualCrossingWeatherApi.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new VisualCrossingWeatherApi.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 4.6
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
    * The HistoricalWeatherApi service constructor.
    * @property {module:api/HistoricalWeatherApi}
    */
    HistoricalWeatherApi,

    /**
    * The TimelineWeatherAPI15DayForecastRequestApi service constructor.
    * @property {module:api/TimelineWeatherAPI15DayForecastRequestApi}
    */
    TimelineWeatherAPI15DayForecastRequestApi,

    /**
    * The TimelineWeatherAPIDateRangeRequestApi service constructor.
    * @property {module:api/TimelineWeatherAPIDateRangeRequestApi}
    */
    TimelineWeatherAPIDateRangeRequestApi,

    /**
    * The TimelineWeatherAPISingleDateRequestApi service constructor.
    * @property {module:api/TimelineWeatherAPISingleDateRequestApi}
    */
    TimelineWeatherAPISingleDateRequestApi,

    /**
    * The WeatherForecastApi service constructor.
    * @property {module:api/WeatherForecastApi}
    */
    WeatherForecastApi
};
