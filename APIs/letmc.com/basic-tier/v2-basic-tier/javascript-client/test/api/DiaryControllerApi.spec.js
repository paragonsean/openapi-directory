/**
 * LetMC Api V2, Basic (Tier 2)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-basic-tier
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
    factory(root.expect, root.LetMcApiV2BasicTier2);
  }
}(this, function(expect, LetMcApiV2BasicTier2) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new LetMcApiV2BasicTier2.DiaryControllerApi();
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

  describe('DiaryControllerApi', function() {
    describe('v2Tier2ShortNameDiaryAllocationsDiaryAllocationIDGet', function() {
      it('should call v2Tier2ShortNameDiaryAllocationsDiaryAllocationIDGet successfully', function(done) {
        //uncomment below and update the code to test v2Tier2ShortNameDiaryAllocationsDiaryAllocationIDGet
        //instance.v2Tier2ShortNameDiaryAllocationsDiaryAllocationIDGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v2Tier2ShortNameDiaryAllocationsGet', function() {
      it('should call v2Tier2ShortNameDiaryAllocationsGet successfully', function(done) {
        //uncomment below and update the code to test v2Tier2ShortNameDiaryAllocationsGet
        //instance.v2Tier2ShortNameDiaryAllocationsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v2Tier2ShortNameDiaryAppointmentsDiaryAppointmentIDGet', function() {
      it('should call v2Tier2ShortNameDiaryAppointmentsDiaryAppointmentIDGet successfully', function(done) {
        //uncomment below and update the code to test v2Tier2ShortNameDiaryAppointmentsDiaryAppointmentIDGet
        //instance.v2Tier2ShortNameDiaryAppointmentsDiaryAppointmentIDGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v2Tier2ShortNameDiaryAppointmentsGet', function() {
      it('should call v2Tier2ShortNameDiaryAppointmentsGet successfully', function(done) {
        //uncomment below and update the code to test v2Tier2ShortNameDiaryAppointmentsGet
        //instance.v2Tier2ShortNameDiaryAppointmentsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v2Tier2ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet', function() {
      it('should call v2Tier2ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet successfully', function(done) {
        //uncomment below and update the code to test v2Tier2ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet
        //instance.v2Tier2ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v2Tier2ShortNameDiaryAppointmenttypesGet', function() {
      it('should call v2Tier2ShortNameDiaryAppointmenttypesGet successfully', function(done) {
        //uncomment below and update the code to test v2Tier2ShortNameDiaryAppointmenttypesGet
        //instance.v2Tier2ShortNameDiaryAppointmenttypesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
