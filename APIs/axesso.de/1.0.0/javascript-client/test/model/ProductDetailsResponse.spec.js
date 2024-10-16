/**
 * Axesso Api
 * Use this api to fetch information to Amazon products and more.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@axesso.de
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
    factory(root.expect, root.AxessoApi);
  }
}(this, function(expect, AxessoApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AxessoApi.ProductDetailsResponse();
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

  describe('ProductDetailsResponse', function() {
    it('should create an instance of ProductDetailsResponse', function() {
      // uncomment below and update the code to test ProductDetailsResponse
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be.a(AxessoApi.ProductDetailsResponse);
    });

    it('should have the property answeredQuestions (base name: "answeredQuestions")', function() {
      // uncomment below and update the code to test the property answeredQuestions
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property asin (base name: "asin")', function() {
      // uncomment below and update the code to test the property asin
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property countReview (base name: "countReview")', function() {
      // uncomment below and update the code to test the property countReview
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property features (base name: "features")', function() {
      // uncomment below and update the code to test the property features
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property fulfilledBy (base name: "fulfilledBy")', function() {
      // uncomment below and update the code to test the property fulfilledBy
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property manufacturer (base name: "manufacturer")', function() {
      // uncomment below and update the code to test the property manufacturer
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property price (base name: "price")', function() {
      // uncomment below and update the code to test the property price
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property priceSaving (base name: "priceSaving")', function() {
      // uncomment below and update the code to test the property priceSaving
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property priceShippingInformation (base name: "priceShippingInformation")', function() {
      // uncomment below and update the code to test the property priceShippingInformation
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property prime (base name: "prime")', function() {
      // uncomment below and update the code to test the property prime
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property productRating (base name: "productRating")', function() {
      // uncomment below and update the code to test the property productRating
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property productTitle (base name: "productTitle")', function() {
      // uncomment below and update the code to test the property productTitle
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property responseMessage (base name: "responseMessage")', function() {
      // uncomment below and update the code to test the property responseMessage
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property responseStatus (base name: "responseStatus")', function() {
      // uncomment below and update the code to test the property responseStatus
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property retailPrice (base name: "retailPrice")', function() {
      // uncomment below and update the code to test the property retailPrice
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property sizeSelection (base name: "sizeSelection")', function() {
      // uncomment below and update the code to test the property sizeSelection
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property soldBy (base name: "soldBy")', function() {
      // uncomment below and update the code to test the property soldBy
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

    it('should have the property warehouseAvailability (base name: "warehouseAvailability")', function() {
      // uncomment below and update the code to test the property warehouseAvailability
      //var instance = new AxessoApi.ProductDetailsResponse();
      //expect(instance).to.be();
    });

  });

}));
