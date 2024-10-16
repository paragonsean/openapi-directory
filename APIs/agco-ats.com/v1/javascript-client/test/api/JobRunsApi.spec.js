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
    instance = new AgcoApi.JobRunsApi();
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

  describe('JobRunsApi', function() {
    describe('jobRunsDeleteJobRun', function() {
      it('should call jobRunsDeleteJobRun successfully', function(done) {
        //uncomment below and update the code to test jobRunsDeleteJobRun
        //instance.jobRunsDeleteJobRun(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('jobRunsGetJobRun', function() {
      it('should call jobRunsGetJobRun successfully', function(done) {
        //uncomment below and update the code to test jobRunsGetJobRun
        //instance.jobRunsGetJobRun(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('jobRunsGetJobRuns', function() {
      it('should call jobRunsGetJobRuns successfully', function(done) {
        //uncomment below and update the code to test jobRunsGetJobRuns
        //instance.jobRunsGetJobRuns(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('jobRunsPostJobRun', function() {
      it('should call jobRunsPostJobRun successfully', function(done) {
        //uncomment below and update the code to test jobRunsPostJobRun
        //instance.jobRunsPostJobRun(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('jobRunsPutJobRun', function() {
      it('should call jobRunsPutJobRun successfully', function(done) {
        //uncomment below and update the code to test jobRunsPutJobRun
        //instance.jobRunsPutJobRun(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
