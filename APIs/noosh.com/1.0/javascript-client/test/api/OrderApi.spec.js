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
    instance = new NooshApiApplication.OrderApi();
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

  describe('OrderApi', function() {
    describe('getBuyOrder', function() {
      it('should call getBuyOrder successfully', function(done) {
        //uncomment below and update the code to test getBuyOrder
        //instance.getBuyOrder(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getBuyOrderList', function() {
      it('should call getBuyOrderList successfully', function(done) {
        //uncomment below and update the code to test getBuyOrderList
        //instance.getBuyOrderList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getBuyOrderListOfWorkgroup', function() {
      it('should call getBuyOrderListOfWorkgroup successfully', function(done) {
        //uncomment below and update the code to test getBuyOrderListOfWorkgroup
        //instance.getBuyOrderListOfWorkgroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getBuyOrderOfWorkgroup', function() {
      it('should call getBuyOrderOfWorkgroup successfully', function(done) {
        //uncomment below and update the code to test getBuyOrderOfWorkgroup
        //instance.getBuyOrderOfWorkgroup(function(error) {
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
    describe('getSellOrder', function() {
      it('should call getSellOrder successfully', function(done) {
        //uncomment below and update the code to test getSellOrder
        //instance.getSellOrder(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getSellOrderList', function() {
      it('should call getSellOrderList successfully', function(done) {
        //uncomment below and update the code to test getSellOrderList
        //instance.getSellOrderList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getSellOrderListOfWorkgroup', function() {
      it('should call getSellOrderListOfWorkgroup successfully', function(done) {
        //uncomment below and update the code to test getSellOrderListOfWorkgroup
        //instance.getSellOrderListOfWorkgroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getSellOrderOfWorkgroup', function() {
      it('should call getSellOrderOfWorkgroup successfully', function(done) {
        //uncomment below and update the code to test getSellOrderOfWorkgroup
        //instance.getSellOrderOfWorkgroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('postBuyOrder', function() {
      it('should call postBuyOrder successfully', function(done) {
        //uncomment below and update the code to test postBuyOrder
        //instance.postBuyOrder(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('putBuyOrder', function() {
      it('should call putBuyOrder successfully', function(done) {
        //uncomment below and update the code to test putBuyOrder
        //instance.putBuyOrder(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('putSellOrder', function() {
      it('should call putSellOrder successfully', function(done) {
        //uncomment below and update the code to test putSellOrder
        //instance.putSellOrder(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
