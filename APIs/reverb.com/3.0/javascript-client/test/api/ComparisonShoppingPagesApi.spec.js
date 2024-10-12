/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
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
    factory(root.expect, root.Reverb);
  }
}(this, function(expect, Reverb) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Reverb.ComparisonShoppingPagesApi();
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

  describe('ComparisonShoppingPagesApi', function() {
    describe('comparisonShoppingPagesFindGet', function() {
      it('should call comparisonShoppingPagesFindGet successfully', function(done) {
        //uncomment below and update the code to test comparisonShoppingPagesFindGet
        //instance.comparisonShoppingPagesFindGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('comparisonShoppingPagesGet', function() {
      it('should call comparisonShoppingPagesGet successfully', function(done) {
        //uncomment below and update the code to test comparisonShoppingPagesGet
        //instance.comparisonShoppingPagesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('comparisonShoppingPagesIdGet', function() {
      it('should call comparisonShoppingPagesIdGet successfully', function(done) {
        //uncomment below and update the code to test comparisonShoppingPagesIdGet
        //instance.comparisonShoppingPagesIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('comparisonShoppingPagesIdListingsGet', function() {
      it('should call comparisonShoppingPagesIdListingsGet successfully', function(done) {
        //uncomment below and update the code to test comparisonShoppingPagesIdListingsGet
        //instance.comparisonShoppingPagesIdListingsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('comparisonShoppingPagesIdReviewsGet', function() {
      it('should call comparisonShoppingPagesIdReviewsGet successfully', function(done) {
        //uncomment below and update the code to test comparisonShoppingPagesIdReviewsGet
        //instance.comparisonShoppingPagesIdReviewsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
