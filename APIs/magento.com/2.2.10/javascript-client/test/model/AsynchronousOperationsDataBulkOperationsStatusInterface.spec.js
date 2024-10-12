/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
    factory(root.expect, root.MagentoB2B);
  }
}(this, function(expect, MagentoB2B) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MagentoB2B.AsynchronousOperationsDataBulkOperationsStatusInterface();
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

  describe('AsynchronousOperationsDataBulkOperationsStatusInterface', function() {
    it('should create an instance of AsynchronousOperationsDataBulkOperationsStatusInterface', function() {
      // uncomment below and update the code to test AsynchronousOperationsDataBulkOperationsStatusInterface
      //var instance = new MagentoB2B.AsynchronousOperationsDataBulkOperationsStatusInterface();
      //expect(instance).to.be.a(MagentoB2B.AsynchronousOperationsDataBulkOperationsStatusInterface);
    });

    it('should have the property bulkId (base name: "bulk_id")', function() {
      // uncomment below and update the code to test the property bulkId
      //var instance = new MagentoB2B.AsynchronousOperationsDataBulkOperationsStatusInterface();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new MagentoB2B.AsynchronousOperationsDataBulkOperationsStatusInterface();
      //expect(instance).to.be();
    });

    it('should have the property extensionAttributes (base name: "extension_attributes")', function() {
      // uncomment below and update the code to test the property extensionAttributes
      //var instance = new MagentoB2B.AsynchronousOperationsDataBulkOperationsStatusInterface();
      //expect(instance).to.be();
    });

    it('should have the property operationCount (base name: "operation_count")', function() {
      // uncomment below and update the code to test the property operationCount
      //var instance = new MagentoB2B.AsynchronousOperationsDataBulkOperationsStatusInterface();
      //expect(instance).to.be();
    });

    it('should have the property operationsList (base name: "operations_list")', function() {
      // uncomment below and update the code to test the property operationsList
      //var instance = new MagentoB2B.AsynchronousOperationsDataBulkOperationsStatusInterface();
      //expect(instance).to.be();
    });

    it('should have the property startTime (base name: "start_time")', function() {
      // uncomment below and update the code to test the property startTime
      //var instance = new MagentoB2B.AsynchronousOperationsDataBulkOperationsStatusInterface();
      //expect(instance).to.be();
    });

    it('should have the property userId (base name: "user_id")', function() {
      // uncomment below and update the code to test the property userId
      //var instance = new MagentoB2B.AsynchronousOperationsDataBulkOperationsStatusInterface();
      //expect(instance).to.be();
    });

  });

}));
