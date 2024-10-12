/**
 * Voodoo Manufacturing 3D Print API
 * Welcome to the Voodoo Manufacturing API docs!  Your Voodoo Manufacturing API key must be included with each request to the API. The API will look for the key in the \"api_key\" header of the request. <a href=\"https://voodoomfg.com/3d-print-api#get-access\" target=\"_blank\">You can request a key here.</a>  This API provides a programmatic interface for submitting printing orders to Voodoo Manufacturing. The general process for creating an order is as follows:   - Get a list of the available materials with the /materials endpoint   - Upload models to the API with the /models endpoint   - Get quotes for shipping methods with the /order/shipping endpoint   - Get a quote for an order with the /order/create endpoint   - Confirm the order with the /order/confirm endpoint  Uploaded models and orders can be retrieved either in bulk or by id at the /model and /order endpoints, respectively.  In some cases, you may wish to get a quote for a specific model without the context of an order. In this case, you may use the /model/quote (if you've already uploaded the model to the API) or the /model/quote_attrs (lets you quote based on calculated model attributes) endpoints. 
 *
 * The version of the OpenAPI document: 2.0.0
 * Contact: support@voodoomfg.com
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
    factory(root.expect, root.VoodooManufacturing3DPrintApi);
  }
}(this, function(expect, VoodooManufacturing3DPrintApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new VoodooManufacturing3DPrintApi.Rate();
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

  describe('Rate', function() {
    it('should create an instance of Rate', function() {
      // uncomment below and update the code to test Rate
      //var instance = new VoodooManufacturing3DPrintApi.Rate();
      //expect(instance).to.be.a(VoodooManufacturing3DPrintApi.Rate);
    });

    it('should have the property deliveryDate (base name: "delivery_date")', function() {
      // uncomment below and update the code to test the property deliveryDate
      //var instance = new VoodooManufacturing3DPrintApi.Rate();
      //expect(instance).to.be();
    });

    it('should have the property displayName (base name: "display_name")', function() {
      // uncomment below and update the code to test the property displayName
      //var instance = new VoodooManufacturing3DPrintApi.Rate();
      //expect(instance).to.be();
    });

    it('should have the property guaranteed (base name: "guaranteed")', function() {
      // uncomment below and update the code to test the property guaranteed
      //var instance = new VoodooManufacturing3DPrintApi.Rate();
      //expect(instance).to.be();
    });

    it('should have the property price (base name: "price")', function() {
      // uncomment below and update the code to test the property price
      //var instance = new VoodooManufacturing3DPrintApi.Rate();
      //expect(instance).to.be();
    });

    it('should have the property service (base name: "service")', function() {
      // uncomment below and update the code to test the property service
      //var instance = new VoodooManufacturing3DPrintApi.Rate();
      //expect(instance).to.be();
    });

    it('should have the property shipDate (base name: "ship_date")', function() {
      // uncomment below and update the code to test the property shipDate
      //var instance = new VoodooManufacturing3DPrintApi.Rate();
      //expect(instance).to.be();
    });

    it('should have the property value (base name: "value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new VoodooManufacturing3DPrintApi.Rate();
      //expect(instance).to.be();
    });

  });

}));
