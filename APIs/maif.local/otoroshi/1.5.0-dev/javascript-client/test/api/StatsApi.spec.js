/**
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
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
    factory(root.expect, root.OtoroshiAdminApi);
  }
}(this, function(expect, OtoroshiAdminApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new OtoroshiAdminApi.StatsApi();
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

  describe('StatsApi', function() {
    describe('globalLiveStats', function() {
      it('should call globalLiveStats successfully', function(done) {
        //uncomment below and update the code to test globalLiveStats
        //instance.globalLiveStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('serviceLiveStats', function() {
      it('should call serviceLiveStats successfully', function(done) {
        //uncomment below and update the code to test serviceLiveStats
        //instance.serviceLiveStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
