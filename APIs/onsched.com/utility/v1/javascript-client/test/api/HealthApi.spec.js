/**
 * OnSched API Utility
 * Endpoints for system utilities. e.g.Health
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.OnSchedApiUtility);
  }
}(this, function(expect, OnSchedApiUtility) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new OnSchedApiUtility.HealthApi();
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

  describe('HealthApi', function() {
    describe('utilityV1HealthHeartbeatGet', function() {
      it('should call utilityV1HealthHeartbeatGet successfully', function(done) {
        //uncomment below and update the code to test utilityV1HealthHeartbeatGet
        //instance.utilityV1HealthHeartbeatGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('utilityV1HealthThreadinfoGet', function() {
      it('should call utilityV1HealthThreadinfoGet successfully', function(done) {
        //uncomment below and update the code to test utilityV1HealthThreadinfoGet
        //instance.utilityV1HealthThreadinfoGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
