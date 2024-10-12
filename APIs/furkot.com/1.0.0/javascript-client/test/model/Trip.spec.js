/**
 * Furkot Trips
 * Furkot provides Rest API to access user trip data. Using Furkot API an application can list user trips and display stops for a specific trip. Furkot API uses OAuth2 protocol to authorize applications to access data on behalf of users. 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: trips@furkot.com
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
    factory(root.expect, root.FurkotTrips);
  }
}(this, function(expect, FurkotTrips) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FurkotTrips.Trip();
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

  describe('Trip', function() {
    it('should create an instance of Trip', function() {
      // uncomment below and update the code to test Trip
      //var instance = new FurkotTrips.Trip();
      //expect(instance).to.be.a(FurkotTrips.Trip);
    });

    it('should have the property begin (base name: "begin")', function() {
      // uncomment below and update the code to test the property begin
      //var instance = new FurkotTrips.Trip();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new FurkotTrips.Trip();
      //expect(instance).to.be();
    });

    it('should have the property end (base name: "end")', function() {
      // uncomment below and update the code to test the property end
      //var instance = new FurkotTrips.Trip();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new FurkotTrips.Trip();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new FurkotTrips.Trip();
      //expect(instance).to.be();
    });

  });

}));
