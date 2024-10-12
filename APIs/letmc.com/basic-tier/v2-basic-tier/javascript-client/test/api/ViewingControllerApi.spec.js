/**
 * LetMC Api V2, Basic (Tier 2)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-basic-tier
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
    factory(root.expect, root.LetMcApiV2BasicTier2);
  }
}(this, function(expect, LetMcApiV2BasicTier2) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new LetMcApiV2BasicTier2.ViewingControllerApi();
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

  describe('ViewingControllerApi', function() {
    describe('viewingControllerGetBookings', function() {
      it('should call viewingControllerGetBookings successfully', function(done) {
        //uncomment below and update the code to test viewingControllerGetBookings
        //instance.viewingControllerGetBookings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('viewingControllerMakeBooking', function() {
      it('should call viewingControllerMakeBooking successfully', function(done) {
        //uncomment below and update the code to test viewingControllerMakeBooking
        //instance.viewingControllerMakeBooking(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
