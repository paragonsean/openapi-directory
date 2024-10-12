/**
 * Noosh API application
 * Full description of Noosh API
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
    factory(root.expect, root.NooshApiApplication);
  }
}(this, function(expect, NooshApiApplication) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NooshApiApplication.RfqItemBaseVO();
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

  describe('RfqItemBaseVO', function() {
    it('should create an instance of RfqItemBaseVO', function() {
      // uncomment below and update the code to test RfqItemBaseVO
      //var instance = new NooshApiApplication.RfqItemBaseVO();
      //expect(instance).to.be.a(NooshApiApplication.RfqItemBaseVO);
    });

    it('should have the property jobId (base name: "job_id")', function() {
      // uncomment below and update the code to test the property jobId
      //var instance = new NooshApiApplication.RfqItemBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property rfqItemId (base name: "rfq_item_id")', function() {
      // uncomment below and update the code to test the property rfqItemId
      //var instance = new NooshApiApplication.RfqItemBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property spec (base name: "spec")', function() {
      // uncomment below and update the code to test the property spec
      //var instance = new NooshApiApplication.RfqItemBaseVO();
      //expect(instance).to.be();
    });

  });

}));
