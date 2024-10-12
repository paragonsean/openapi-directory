/**
 * Fahrplan-Free
 * A RESTful webservice to request a railway journey - FREE plan with restricted access (max. 10 requests per minute). Please ignore the message in the API Console about the access token.  Register to use an less restricted version, which requires an access token.
 *
 * The version of the OpenAPI document: v1
 * Contact: DBOpenData@deutschebahn.com
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
    factory(root.expect, root.FahrplanFree);
  }
}(this, function(expect, FahrplanFree) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FahrplanFree.Location();
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

  describe('Location', function() {
    it('should create an instance of Location', function() {
      // uncomment below and update the code to test Location
      //var instance = new FahrplanFree.Location();
      //expect(instance).to.be.a(FahrplanFree.Location);
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new FahrplanFree.Location();
      //expect(instance).to.be();
    });

    it('should have the property lat (base name: "lat")', function() {
      // uncomment below and update the code to test the property lat
      //var instance = new FahrplanFree.Location();
      //expect(instance).to.be();
    });

    it('should have the property lon (base name: "lon")', function() {
      // uncomment below and update the code to test the property lon
      //var instance = new FahrplanFree.Location();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new FahrplanFree.Location();
      //expect(instance).to.be();
    });

  });

}));
