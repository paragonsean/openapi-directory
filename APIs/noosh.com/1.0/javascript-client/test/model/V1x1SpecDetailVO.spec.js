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
    instance = new NooshApiApplication.V1x1SpecDetailVO();
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

  describe('V1x1SpecDetailVO', function() {
    it('should create an instance of V1x1SpecDetailVO', function() {
      // uncomment below and update the code to test V1x1SpecDetailVO
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be.a(NooshApiApplication.V1x1SpecDetailVO);
    });

    it('should have the property clientStatus (base name: "client_status")', function() {
      // uncomment below and update the code to test the property clientStatus
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property createDate (base name: "create_date")', function() {
      // uncomment below and update the code to test the property createDate
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property createdBy (base name: "created_by")', function() {
      // uncomment below and update the code to test the property createdBy
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property firstLevelCustomFields (base name: "first_level_custom_fields")', function() {
      // uncomment below and update the code to test the property firstLevelCustomFields
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property headerCustomFields (base name: "header_custom_fields")', function() {
      // uncomment below and update the code to test the property headerCustomFields
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property jobId (base name: "job_id")', function() {
      // uncomment below and update the code to test the property jobId
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property lastUpdated (base name: "last_updated")', function() {
      // uncomment below and update the code to test the property lastUpdated
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property productType (base name: "product_type")', function() {
      // uncomment below and update the code to test the property productType
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property productTypeInfo (base name: "product_type_info")', function() {
      // uncomment below and update the code to test the property productTypeInfo
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property quantity1 (base name: "quantity_1")', function() {
      // uncomment below and update the code to test the property quantity1
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property quantity2 (base name: "quantity_2")', function() {
      // uncomment below and update the code to test the property quantity2
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property quantity3 (base name: "quantity_3")', function() {
      // uncomment below and update the code to test the property quantity3
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property quantity4 (base name: "quantity_4")', function() {
      // uncomment below and update the code to test the property quantity4
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property quantity5 (base name: "quantity_5")', function() {
      // uncomment below and update the code to test the property quantity5
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property referenceNumber (base name: "reference_number")', function() {
      // uncomment below and update the code to test the property referenceNumber
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property secondLevelCustomFields (base name: "second_level_custom_fields")', function() {
      // uncomment below and update the code to test the property secondLevelCustomFields
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property sku (base name: "sku")', function() {
      // uncomment below and update the code to test the property sku
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property specId (base name: "spec_id")', function() {
      // uncomment below and update the code to test the property specId
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property specName (base name: "spec_name")', function() {
      // uncomment below and update the code to test the property specName
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property specOptions (base name: "spec_options")', function() {
      // uncomment below and update the code to test the property specOptions
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property specOptionsComplete (base name: "spec_options_complete")', function() {
      // uncomment below and update the code to test the property specOptionsComplete
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property specOriginal (base name: "spec_original")', function() {
      // uncomment below and update the code to test the property specOriginal
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property specType (base name: "spec_type")', function() {
      // uncomment below and update the code to test the property specType
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property supplierStatus (base name: "supplier_status")', function() {
      // uncomment below and update the code to test the property supplierStatus
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property uofms (base name: "uofms")', function() {
      // uncomment below and update the code to test the property uofms
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property userState (base name: "user_state")', function() {
      // uncomment below and update the code to test the property userState
      //var instance = new NooshApiApplication.V1x1SpecDetailVO();
      //expect(instance).to.be();
    });

  });

}));
