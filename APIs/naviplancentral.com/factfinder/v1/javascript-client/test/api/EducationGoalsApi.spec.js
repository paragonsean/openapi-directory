/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
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
    factory(root.expect, root.AdvicentFactFinderService);
  }
}(this, function(expect, AdvicentFactFinderService) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AdvicentFactFinderService.EducationGoalsApi();
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

  describe('EducationGoalsApi', function() {
    describe('educationGoalsDeleteByEducationgoalidId', function() {
      it('should call educationGoalsDeleteByEducationgoalidId successfully', function(done) {
        //uncomment below and update the code to test educationGoalsDeleteByEducationgoalidId
        //instance.educationGoalsDeleteByEducationgoalidId(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('educationGoalsDeleteById', function() {
      it('should call educationGoalsDeleteById successfully', function(done) {
        //uncomment below and update the code to test educationGoalsDeleteById
        //instance.educationGoalsDeleteById(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('educationGoalsGetById', function() {
      it('should call educationGoalsGetById successfully', function(done) {
        //uncomment below and update the code to test educationGoalsGetById
        //instance.educationGoalsGetById(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('educationGoalsGetEducationExpenseByEducationgoalidId', function() {
      it('should call educationGoalsGetEducationExpenseByEducationgoalidId successfully', function(done) {
        //uncomment below and update the code to test educationGoalsGetEducationExpenseByEducationgoalidId
        //instance.educationGoalsGetEducationExpenseByEducationgoalidId(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid', function() {
      it('should call educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid successfully', function(done) {
        //uncomment below and update the code to test educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid
        //instance.educationGoalsGetEducationExpensesByEducationGoalIdByEducationgoalid(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid', function() {
      it('should call educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid successfully', function(done) {
        //uncomment below and update the code to test educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid
        //instance.educationGoalsGetEducationGoalsByFactFinderIdByFactfinderid(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('educationGoalsPostByEducationgoalidModel', function() {
      it('should call educationGoalsPostByEducationgoalidModel successfully', function(done) {
        //uncomment below and update the code to test educationGoalsPostByEducationgoalidModel
        //instance.educationGoalsPostByEducationgoalidModel(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('educationGoalsPostByModel', function() {
      it('should call educationGoalsPostByModel successfully', function(done) {
        //uncomment below and update the code to test educationGoalsPostByModel
        //instance.educationGoalsPostByModel(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('educationGoalsPutByEducationgoalidIdModel', function() {
      it('should call educationGoalsPutByEducationgoalidIdModel successfully', function(done) {
        //uncomment below and update the code to test educationGoalsPutByEducationgoalidIdModel
        //instance.educationGoalsPutByEducationgoalidIdModel(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('educationGoalsPutByIdModel', function() {
      it('should call educationGoalsPutByIdModel successfully', function(done) {
        //uncomment below and update the code to test educationGoalsPutByIdModel
        //instance.educationGoalsPutByIdModel(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
