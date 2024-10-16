/**
 * agentOS API V3, Maintenance Call Group
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-maintenance
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
    factory(root.expect, root.AgentOsApiV3MaintenanceCallGroup);
  }
}(this, function(expect, AgentOsApiV3MaintenanceCallGroup) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AgentOsApiV3MaintenanceCallGroup.MaintenanceDocumentModel();
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

  describe('MaintenanceDocumentModel', function() {
    it('should create an instance of MaintenanceDocumentModel', function() {
      // uncomment below and update the code to test MaintenanceDocumentModel
      //var instance = new AgentOsApiV3MaintenanceCallGroup.MaintenanceDocumentModel();
      //expect(instance).to.be.a(AgentOsApiV3MaintenanceCallGroup.MaintenanceDocumentModel);
    });

    it('should have the property mimeType (base name: "MimeType")', function() {
      // uncomment below and update the code to test the property mimeType
      //var instance = new AgentOsApiV3MaintenanceCallGroup.MaintenanceDocumentModel();
      //expect(instance).to.be();
    });

    it('should have the property URL (base name: "URL")', function() {
      // uncomment below and update the code to test the property URL
      //var instance = new AgentOsApiV3MaintenanceCallGroup.MaintenanceDocumentModel();
      //expect(instance).to.be();
    });

  });

}));
