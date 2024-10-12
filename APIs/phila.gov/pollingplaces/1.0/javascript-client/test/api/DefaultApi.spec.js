/**
 * Polling Places API
 *  This data set contains the list of polling places. It can be organized by ward/division, accessibility rating, or type of building.  This list is used to assign poll workers, send the machines and necessary accessibility materials, etc.  **Endpoint:** http://api.phila.gov/polling-places/v1 
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
    factory(root.expect, root.PollingPlacesApi);
  }
}(this, function(expect, PollingPlacesApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new PollingPlacesApi.DefaultApi();
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

  describe('DefaultApi', function() {
    describe('rootGet', function() {
      it('should call rootGet successfully', function(done) {
        //uncomment below and update the code to test rootGet
        //instance.rootGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
