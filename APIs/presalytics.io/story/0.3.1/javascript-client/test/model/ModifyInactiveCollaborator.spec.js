/**
 * Story
 * This API is the main entry point for creating, editing and publishing analytics throught the Presalytics API
 *
 * The version of the OpenAPI document: 0.3.1
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
    factory(root.expect, root.Story);
  }
}(this, function(expect, Story) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Story.ModifyInactiveCollaborator();
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

  describe('ModifyInactiveCollaborator', function() {
    it('should create an instance of ModifyInactiveCollaborator', function() {
      // uncomment below and update the code to test ModifyInactiveCollaborator
      //var instance = new Story.ModifyInactiveCollaborator();
      //expect(instance).to.be.a(Story.ModifyInactiveCollaborator);
    });

    it('should have the property action (base name: "action")', function() {
      // uncomment below and update the code to test the property action
      //var instance = new Story.ModifyInactiveCollaborator();
      //expect(instance).to.be();
    });

    it('should have the property leadId (base name: "lead_id")', function() {
      // uncomment below and update the code to test the property leadId
      //var instance = new Story.ModifyInactiveCollaborator();
      //expect(instance).to.be();
    });

    it('should have the property userId (base name: "user_id")', function() {
      // uncomment below and update the code to test the property userId
      //var instance = new Story.ModifyInactiveCollaborator();
      //expect(instance).to.be();
    });

  });

}));
