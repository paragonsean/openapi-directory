/**
 * StorageManagementClient
 * The Admin Storage Management Client.
 *
 * The version of the OpenAPI document: 2015-12-01-preview
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
    factory(root.expect, root.StorageManagementClient);
  }
}(this, function(expect, StorageManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new StorageManagementClient.TableServicesListMetrics200ResponseValueInnerMetricValuesInner();
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

  describe('TableServicesListMetrics200ResponseValueInnerMetricValuesInner', function() {
    it('should create an instance of TableServicesListMetrics200ResponseValueInnerMetricValuesInner', function() {
      // uncomment below and update the code to test TableServicesListMetrics200ResponseValueInnerMetricValuesInner
      //var instance = new StorageManagementClient.TableServicesListMetrics200ResponseValueInnerMetricValuesInner();
      //expect(instance).to.be.a(StorageManagementClient.TableServicesListMetrics200ResponseValueInnerMetricValuesInner);
    });

    it('should have the property average (base name: "average")', function() {
      // uncomment below and update the code to test the property average
      //var instance = new StorageManagementClient.TableServicesListMetrics200ResponseValueInnerMetricValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property count (base name: "count")', function() {
      // uncomment below and update the code to test the property count
      //var instance = new StorageManagementClient.TableServicesListMetrics200ResponseValueInnerMetricValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property maximum (base name: "maximum")', function() {
      // uncomment below and update the code to test the property maximum
      //var instance = new StorageManagementClient.TableServicesListMetrics200ResponseValueInnerMetricValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property minimum (base name: "minimum")', function() {
      // uncomment below and update the code to test the property minimum
      //var instance = new StorageManagementClient.TableServicesListMetrics200ResponseValueInnerMetricValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property properties (base name: "properties")', function() {
      // uncomment below and update the code to test the property properties
      //var instance = new StorageManagementClient.TableServicesListMetrics200ResponseValueInnerMetricValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property timeStamp (base name: "timeStamp")', function() {
      // uncomment below and update the code to test the property timeStamp
      //var instance = new StorageManagementClient.TableServicesListMetrics200ResponseValueInnerMetricValuesInner();
      //expect(instance).to.be();
    });

    it('should have the property total (base name: "total")', function() {
      // uncomment below and update the code to test the property total
      //var instance = new StorageManagementClient.TableServicesListMetrics200ResponseValueInnerMetricValuesInner();
      //expect(instance).to.be();
    });

  });

}));
