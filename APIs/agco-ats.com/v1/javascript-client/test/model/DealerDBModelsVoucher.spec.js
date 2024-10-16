/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.AgcoApi);
  }
}(this, function(expect, AgcoApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AgcoApi.DealerDBModelsVoucher();
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

  describe('DealerDBModelsVoucher', function() {
    it('should create an instance of DealerDBModelsVoucher', function() {
      // uncomment below and update the code to test DealerDBModelsVoucher
      //var instance = new AgcoApi.DealerDBModelsVoucher();
      //expect(instance).to.be.a(AgcoApi.DealerDBModelsVoucher);
    });

    it('should have the property createdDate (base name: "CreatedDate")', function() {
      // uncomment below and update the code to test the property createdDate
      //var instance = new AgcoApi.DealerDBModelsVoucher();
      //expect(instance).to.be();
    });

    it('should have the property dealerCode (base name: "DealerCode")', function() {
      // uncomment below and update the code to test the property dealerCode
      //var instance = new AgcoApi.DealerDBModelsVoucher();
      //expect(instance).to.be();
    });

    it('should have the property deleted (base name: "Deleted")', function() {
      // uncomment below and update the code to test the property deleted
      //var instance = new AgcoApi.DealerDBModelsVoucher();
      //expect(instance).to.be();
    });

    it('should have the property email (base name: "Email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new AgcoApi.DealerDBModelsVoucher();
      //expect(instance).to.be();
    });

    it('should have the property expirationDate (base name: "ExpirationDate")', function() {
      // uncomment below and update the code to test the property expirationDate
      //var instance = new AgcoApi.DealerDBModelsVoucher();
      //expect(instance).to.be();
    });

    it('should have the property licenseTo (base name: "LicenseTo")', function() {
      // uncomment below and update the code to test the property licenseTo
      //var instance = new AgcoApi.DealerDBModelsVoucher();
      //expect(instance).to.be();
    });

    it('should have the property modifiedBy (base name: "ModifiedBy")', function() {
      // uncomment below and update the code to test the property modifiedBy
      //var instance = new AgcoApi.DealerDBModelsVoucher();
      //expect(instance).to.be();
    });

    it('should have the property orderNumber (base name: "OrderNumber")', function() {
      // uncomment below and update the code to test the property orderNumber
      //var instance = new AgcoApi.DealerDBModelsVoucher();
      //expect(instance).to.be();
    });

    it('should have the property punched (base name: "Punched")', function() {
      // uncomment below and update the code to test the property punched
      //var instance = new AgcoApi.DealerDBModelsVoucher();
      //expect(instance).to.be();
    });

    it('should have the property punchedDate (base name: "PunchedDate")', function() {
      // uncomment below and update the code to test the property punchedDate
      //var instance = new AgcoApi.DealerDBModelsVoucher();
      //expect(instance).to.be();
    });

    it('should have the property purpose (base name: "Purpose")', function() {
      // uncomment below and update the code to test the property purpose
      //var instance = new AgcoApi.DealerDBModelsVoucher();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "Type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new AgcoApi.DealerDBModelsVoucher();
      //expect(instance).to.be();
    });

    it('should have the property voucherCode (base name: "VoucherCode")', function() {
      // uncomment below and update the code to test the property voucherCode
      //var instance = new AgcoApi.DealerDBModelsVoucher();
      //expect(instance).to.be();
    });

  });

}));
