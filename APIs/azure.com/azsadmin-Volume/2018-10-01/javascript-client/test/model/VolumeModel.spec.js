/**
 * FabricAdminClient
 * Volume operation endpoints and objects.
 *
 * The version of the OpenAPI document: 2018-10-01
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
    factory(root.expect, root.FabricAdminClient);
  }
}(this, function(expect, FabricAdminClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FabricAdminClient.VolumeModel();
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

  describe('VolumeModel', function() {
    it('should create an instance of VolumeModel', function() {
      // uncomment below and update the code to test VolumeModel
      //var instance = new FabricAdminClient.VolumeModel();
      //expect(instance).to.be.a(FabricAdminClient.VolumeModel);
    });

    it('should have the property action (base name: "action")', function() {
      // uncomment below and update the code to test the property action
      //var instance = new FabricAdminClient.VolumeModel();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new FabricAdminClient.VolumeModel();
      //expect(instance).to.be();
    });

    it('should have the property healthStatus (base name: "healthStatus")', function() {
      // uncomment below and update the code to test the property healthStatus
      //var instance = new FabricAdminClient.VolumeModel();
      //expect(instance).to.be();
    });

    it('should have the property operationalStatus (base name: "operationalStatus")', function() {
      // uncomment below and update the code to test the property operationalStatus
      //var instance = new FabricAdminClient.VolumeModel();
      //expect(instance).to.be();
    });

    it('should have the property remainingCapacityGB (base name: "remainingCapacityGB")', function() {
      // uncomment below and update the code to test the property remainingCapacityGB
      //var instance = new FabricAdminClient.VolumeModel();
      //expect(instance).to.be();
    });

    it('should have the property repairStatus (base name: "repairStatus")', function() {
      // uncomment below and update the code to test the property repairStatus
      //var instance = new FabricAdminClient.VolumeModel();
      //expect(instance).to.be();
    });

    it('should have the property totalCapacityGB (base name: "totalCapacityGB")', function() {
      // uncomment below and update the code to test the property totalCapacityGB
      //var instance = new FabricAdminClient.VolumeModel();
      //expect(instance).to.be();
    });

    it('should have the property volumeLabel (base name: "volumeLabel")', function() {
      // uncomment below and update the code to test the property volumeLabel
      //var instance = new FabricAdminClient.VolumeModel();
      //expect(instance).to.be();
    });

  });

}));
