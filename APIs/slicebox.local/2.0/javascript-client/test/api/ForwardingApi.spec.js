/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
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
    factory(root.expect, root.SliceboxApi);
  }
}(this, function(expect, SliceboxApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SliceboxApi.ForwardingApi();
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

  describe('ForwardingApi', function() {
    describe('forwardingRuleIdDelete', function() {
      it('should call forwardingRuleIdDelete successfully', function(done) {
        //uncomment below and update the code to test forwardingRuleIdDelete
        //instance.forwardingRuleIdDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('forwardingRulesGet', function() {
      it('should call forwardingRulesGet successfully', function(done) {
        //uncomment below and update the code to test forwardingRulesGet
        //instance.forwardingRulesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('forwardingRulesPost', function() {
      it('should call forwardingRulesPost successfully', function(done) {
        //uncomment below and update the code to test forwardingRulesPost
        //instance.forwardingRulesPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
