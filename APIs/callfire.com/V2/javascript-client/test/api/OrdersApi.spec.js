/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
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
    factory(root.expect, root.CallFireApiDocumentation);
  }
}(this, function(expect, CallFireApiDocumentation) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CallFireApiDocumentation.OrdersApi();
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

  describe('OrdersApi', function() {
    describe('findOrders', function() {
      it('should call findOrders successfully', function(done) {
        //uncomment below and update the code to test findOrders
        //instance.findOrders(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getOrder', function() {
      it('should call getOrder successfully', function(done) {
        //uncomment below and update the code to test getOrder
        //instance.getOrder(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('orderKeywords', function() {
      it('should call orderKeywords successfully', function(done) {
        //uncomment below and update the code to test orderKeywords
        //instance.orderKeywords(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('orderNumbers', function() {
      it('should call orderNumbers successfully', function(done) {
        //uncomment below and update the code to test orderNumbers
        //instance.orderNumbers(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
