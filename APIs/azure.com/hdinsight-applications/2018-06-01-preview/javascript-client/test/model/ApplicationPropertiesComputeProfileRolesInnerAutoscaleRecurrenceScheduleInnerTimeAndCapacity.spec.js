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
    instance = new HdInsightManagementClient.ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity();
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

  describe('ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity', function() {
    it('should create an instance of ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity', function() {
      // uncomment below and update the code to test ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity
      //var instance = new HdInsightManagementClient.ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity();
      //expect(instance).to.be.a(HdInsightManagementClient.ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity);
    });

    it('should have the property maxInstanceCount (base name: "maxInstanceCount")', function() {
      // uncomment below and update the code to test the property maxInstanceCount
      //var instance = new HdInsightManagementClient.ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity();
      //expect(instance).to.be();
    });

    it('should have the property minInstanceCount (base name: "minInstanceCount")', function() {
      // uncomment below and update the code to test the property minInstanceCount
      //var instance = new HdInsightManagementClient.ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity();
      //expect(instance).to.be();
    });

    it('should have the property time (base name: "time")', function() {
      // uncomment below and update the code to test the property time
      //var instance = new HdInsightManagementClient.ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity();
      //expect(instance).to.be();
    });

  });

}));
