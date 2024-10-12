/**
 * EtMDB REST API v1
 * The Ethiopian Movie Database
 *
 * The version of the OpenAPI document: 1.0.0
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
    factory(root.expect, root.EtMdbRestApiV1);
  }
}(this, function(expect, EtMdbRestApiV1) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new EtMdbRestApiV1.CinemaScheduleApi();
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

  describe('CinemaScheduleApi', function() {
    describe('cinemaScheduleSearchRead', function() {
      it('should call cinemaScheduleSearchRead successfully', function(done) {
        //uncomment below and update the code to test cinemaScheduleSearchRead
        //instance.cinemaScheduleSearchRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('cinemaScheduleSearchallRead', function() {
      it('should call cinemaScheduleSearchallRead successfully', function(done) {
        //uncomment below and update the code to test cinemaScheduleSearchallRead
        //instance.cinemaScheduleSearchallRead(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
