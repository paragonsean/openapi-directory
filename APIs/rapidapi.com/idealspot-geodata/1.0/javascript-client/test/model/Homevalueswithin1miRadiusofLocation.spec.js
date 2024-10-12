/**
 * IdealSpot GeoData
 * Hyperlocal Demographics, Vehicle Traffic, Economic, Market Signals, and More. Use this API to request IdealSpot hyperlocal geospatial market insight and geometry data.   ## Detailed Description  Use this API as your **local economy microscope** by querying [IdealSpot](https://www.idealspot.com) hyperlocal market insight and geometry data. We offer the most precise, extensive, and frequently-updated local market data in the US. Our data is available across the entire US and can be queried at geographic scales ranging from the micro (Census block) through the macro (nation).  Better data and analysis leads to a better understanding of local market opportunities and risks. Integrate with your commercial real estate and marketing applications, machine learning workflows, and other investment analytics.  Our goal is to offer the most complete snapshot of the geographically distributed consumer and retail economy. We start with the fundamentals of consumers and business establishments. To connect retailers with consumers, we provide mobility data like vehicle traffic and mobile device data. To describe consumer intent, we provide geolocated digital marketing data.   We believe that accurate capital allocation through reliable local market data is foundational to creating robust, healthy, and livable communities for all. We hope you and your clients find tremendous value in this service.  ## Features  Query data and GeoJSON geometries at these scales for any US latitude and longitude:  * Rings (0.5 km+) * Drive time (1-60 minutes) * Bike time (3-60 minutes) * Walk time (5-60 minutes) * Public transit time (5-60 minutes) * Administrative region (US, states, core-based statistical areas, counties, Census-designated places, Census tracts, zipcodes, Census block groups, opportunity zones)  | Data Feature | Description | | ------- | ------------------------------| | Demographics, Housing, Spending | *Updated Quarterly*.  Current and historical market data including population, spending, and housing. Vendor (PopStats) is relied upon by Walgreens, Ulta Beauty, Blackstone, etc | | Labor, Business Establishments, Economic Conditions | *Updated Quarterly*.  Traditional market data including workforce, business establishment counts, and economic conditions like local GDP, unemployment rates. Vendor (PopStats) is relied upon by Walgreens, Ulta Beauty, Blackstone, etc | | Consumer segmentation | *Updated Annually*. Demographics grouped into narrative-oriented segments. | | Vehicle Traffic | *Updated semi-annually*. Gold standard in vehicle traffic data from INRIX. Counts by day of week, time of day and side of street. | | Rings and Travel time polygons | *Estimate in Real-time*. Rings alongside drive time, walk time, bike time, and public transit time polygons. Request as GeoJSON geometries for mapping or use with data queries | | Administrative region polygons | *Updated Annually*. GeoJSON administrative regions from US Census Bureau: block groups, tracts, counties, CBSAs, states, opportunity zones, USPS zipcodes | | Internet Search Volumes | 30 day rolling averages for geolocated advertising potential across 450 business categories from major search engines | | Social Media Interest | 30 day rolling average for geolocated advertising potential across 450 business categories from major social networks |  ### Coming Soon!  This API powers our local market research platform at [IdealSpot.com](https://www.idealspot.com). The functionality exposed so far is only a portion of our current capabilities. We will be exposing additional API features in time so watch this space!  | Data Feature | Description | | ------- | ------------------------------| Mobile device visit counts, points of interest, brands | Fresh point of interest data across 3000+ brands, millions of POI, and historical foot traffic counts using mobile data for those points of interest Origin/destination trips from mobile devices | Map origins and destinations of devices visiting an arbitrary catchment area Competition search | Search all major point-of-interest aggregators in one query Environment/climate | Expected weather patterns like temperature and precipitation Filter search API | Query data for all counties in state, all tracts in MSA, etc Road segment tiles | Plot road segments on maps in interactive applications  ## Developer Website  For more detail see https://developer.idealspot.com/
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.IdealSpotGeoData);
  }
}(this, function(expect, IdealSpotGeoData) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new IdealSpotGeoData.Homevalueswithin1miRadiusofLocation();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('Homevalueswithin1miRadiusofLocation', function() {
    it('should create an instance of Homevalueswithin1miRadiusofLocation', function() {
      // uncomment below and update the code to test Homevalueswithin1miRadiusofLocation
      //var instance = new IdealSpotGeoData.Homevalueswithin1miRadiusofLocation();
      //expect(instance).to.be.a(IdealSpotGeoData.Homevalueswithin1miRadiusofLocation);
    });

    it('should have the property data (base name: "data")', function() {
      // uncomment below and update the code to test the property data
      //var instance = new IdealSpotGeoData.Homevalueswithin1miRadiusofLocation();
      //expect(instance).to.be();
    });

  });

}));
