/**
 * Personnel Data
 * API for reading and writing personnel data incl. data about attendances and absences
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
    factory(root.expect, root.PersonnelData);
  }
}(this, function(expect, PersonnelData) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new PersonnelData.DefaultApi();
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

  describe('DefaultApi', function() {
    describe('companyAttendancesGet', function() {
      it('should call companyAttendancesGet successfully', function(done) {
        //uncomment below and update the code to test companyAttendancesGet
        //instance.companyAttendancesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('companyAttendancesIdDelete', function() {
      it('should call companyAttendancesIdDelete successfully', function(done) {
        //uncomment below and update the code to test companyAttendancesIdDelete
        //instance.companyAttendancesIdDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('companyAttendancesIdPatch', function() {
      it('should call companyAttendancesIdPatch successfully', function(done) {
        //uncomment below and update the code to test companyAttendancesIdPatch
        //instance.companyAttendancesIdPatch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('companyAttendancesPost', function() {
      it('should call companyAttendancesPost successfully', function(done) {
        //uncomment below and update the code to test companyAttendancesPost
        //instance.companyAttendancesPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('companyEmployeesEmployeeIdGet', function() {
      it('should call companyEmployeesEmployeeIdGet successfully', function(done) {
        //uncomment below and update the code to test companyEmployeesEmployeeIdGet
        //instance.companyEmployeesEmployeeIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('companyEmployeesEmployeeIdProfilePictureWidthGet', function() {
      it('should call companyEmployeesEmployeeIdProfilePictureWidthGet successfully', function(done) {
        //uncomment below and update the code to test companyEmployeesEmployeeIdProfilePictureWidthGet
        //instance.companyEmployeesEmployeeIdProfilePictureWidthGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('companyEmployeesGet', function() {
      it('should call companyEmployeesGet successfully', function(done) {
        //uncomment below and update the code to test companyEmployeesGet
        //instance.companyEmployeesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('companyEmployeesPost', function() {
      it('should call companyEmployeesPost successfully', function(done) {
        //uncomment below and update the code to test companyEmployeesPost
        //instance.companyEmployeesPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('companyTimeOffTypesGet', function() {
      it('should call companyTimeOffTypesGet successfully', function(done) {
        //uncomment below and update the code to test companyTimeOffTypesGet
        //instance.companyTimeOffTypesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('companyTimeOffsGet', function() {
      it('should call companyTimeOffsGet successfully', function(done) {
        //uncomment below and update the code to test companyTimeOffsGet
        //instance.companyTimeOffsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('companyTimeOffsIdDelete', function() {
      it('should call companyTimeOffsIdDelete successfully', function(done) {
        //uncomment below and update the code to test companyTimeOffsIdDelete
        //instance.companyTimeOffsIdDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('companyTimeOffsIdGet', function() {
      it('should call companyTimeOffsIdGet successfully', function(done) {
        //uncomment below and update the code to test companyTimeOffsIdGet
        //instance.companyTimeOffsIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('companyTimeOffsPost', function() {
      it('should call companyTimeOffsPost successfully', function(done) {
        //uncomment below and update the code to test companyTimeOffsPost
        //instance.companyTimeOffsPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
