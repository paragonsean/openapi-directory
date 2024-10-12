/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
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
    factory(root.expect, root.Gateway);
  }
}(this, function(expect, Gateway) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Gateway.DataFlowApi();
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

  describe('DataFlowApi', function() {
    describe('v05HealthInformationCmOnRequestPost', function() {
      it('should call v05HealthInformationCmOnRequestPost successfully', function(done) {
        //uncomment below and update the code to test v05HealthInformationCmOnRequestPost
        //instance.v05HealthInformationCmOnRequestPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v05HealthInformationCmRequestPost', function() {
      it('should call v05HealthInformationCmRequestPost successfully', function(done) {
        //uncomment below and update the code to test v05HealthInformationCmRequestPost
        //instance.v05HealthInformationCmRequestPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v05HealthInformationHipOnRequestPost', function() {
      it('should call v05HealthInformationHipOnRequestPost successfully', function(done) {
        //uncomment below and update the code to test v05HealthInformationHipOnRequestPost
        //instance.v05HealthInformationHipOnRequestPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v05HealthInformationHipRequestPost', function() {
      it('should call v05HealthInformationHipRequestPost successfully', function(done) {
        //uncomment below and update the code to test v05HealthInformationHipRequestPost
        //instance.v05HealthInformationHipRequestPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v05HealthInformationNotifyPost', function() {
      it('should call v05HealthInformationNotifyPost successfully', function(done) {
        //uncomment below and update the code to test v05HealthInformationNotifyPost
        //instance.v05HealthInformationNotifyPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
