/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
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
    factory(root.expect, root.HdInsightManagementClient);
  }
}(this, function(expect, HdInsightManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new HdInsightManagementClient.ApplicationPropertiesErrorsInner();
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

  describe('ApplicationPropertiesErrorsInner', function() {
    it('should create an instance of ApplicationPropertiesErrorsInner', function() {
      // uncomment below and update the code to test ApplicationPropertiesErrorsInner
      //var instance = new HdInsightManagementClient.ApplicationPropertiesErrorsInner();
      //expect(instance).to.be.a(HdInsightManagementClient.ApplicationPropertiesErrorsInner);
    });

    it('should have the property code (base name: "code")', function() {
      // uncomment below and update the code to test the property code
      //var instance = new HdInsightManagementClient.ApplicationPropertiesErrorsInner();
      //expect(instance).to.be();
    });

    it('should have the property message (base name: "message")', function() {
      // uncomment below and update the code to test the property message
      //var instance = new HdInsightManagementClient.ApplicationPropertiesErrorsInner();
      //expect(instance).to.be();
    });

  });

}));
