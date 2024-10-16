/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
    factory(root.expect, root.AppCenterClient);
  }
}(this, function(expect, AppCenterClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AppCenterClient.AnalyticsApi();
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

  describe('AnalyticsApi', function() {
    describe('analyticsAudienceNameExists', function() {
      it('should call analyticsAudienceNameExists successfully', function(done) {
        //uncomment below and update the code to test analyticsAudienceNameExists
        //instance.analyticsAudienceNameExists(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsCrashCounts', function() {
      it('should call analyticsCrashCounts successfully', function(done) {
        //uncomment below and update the code to test analyticsCrashCounts
        //instance.analyticsCrashCounts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsCrashFreeDevicePercentages', function() {
      it('should call analyticsCrashFreeDevicePercentages successfully', function(done) {
        //uncomment below and update the code to test analyticsCrashFreeDevicePercentages
        //instance.analyticsCrashFreeDevicePercentages(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsCrashGroupCounts', function() {
      it('should call analyticsCrashGroupCounts successfully', function(done) {
        //uncomment below and update the code to test analyticsCrashGroupCounts
        //instance.analyticsCrashGroupCounts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsCrashGroupModelCounts', function() {
      it('should call analyticsCrashGroupModelCounts successfully', function(done) {
        //uncomment below and update the code to test analyticsCrashGroupModelCounts
        //instance.analyticsCrashGroupModelCounts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsCrashGroupOperatingSystemCounts', function() {
      it('should call analyticsCrashGroupOperatingSystemCounts successfully', function(done) {
        //uncomment below and update the code to test analyticsCrashGroupOperatingSystemCounts
        //instance.analyticsCrashGroupOperatingSystemCounts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsCrashGroupTotals', function() {
      it('should call analyticsCrashGroupTotals successfully', function(done) {
        //uncomment below and update the code to test analyticsCrashGroupTotals
        //instance.analyticsCrashGroupTotals(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsCrashGroupsTotals', function() {
      it('should call analyticsCrashGroupsTotals successfully', function(done) {
        //uncomment below and update the code to test analyticsCrashGroupsTotals
        //instance.analyticsCrashGroupsTotals(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsCreateOrUpdateAudience', function() {
      it('should call analyticsCreateOrUpdateAudience successfully', function(done) {
        //uncomment below and update the code to test analyticsCreateOrUpdateAudience
        //instance.analyticsCreateOrUpdateAudience(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsDeleteAudience', function() {
      it('should call analyticsDeleteAudience successfully', function(done) {
        //uncomment below and update the code to test analyticsDeleteAudience
        //instance.analyticsDeleteAudience(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsDeviceCounts', function() {
      it('should call analyticsDeviceCounts successfully', function(done) {
        //uncomment below and update the code to test analyticsDeviceCounts
        //instance.analyticsDeviceCounts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsDistributionReleaseCounts', function() {
      it('should call analyticsDistributionReleaseCounts successfully', function(done) {
        //uncomment below and update the code to test analyticsDistributionReleaseCounts
        //instance.analyticsDistributionReleaseCounts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsEventCount', function() {
      it('should call analyticsEventCount successfully', function(done) {
        //uncomment below and update the code to test analyticsEventCount
        //instance.analyticsEventCount(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsEventDeviceCount', function() {
      it('should call analyticsEventDeviceCount successfully', function(done) {
        //uncomment below and update the code to test analyticsEventDeviceCount
        //instance.analyticsEventDeviceCount(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsEventPerDeviceCount', function() {
      it('should call analyticsEventPerDeviceCount successfully', function(done) {
        //uncomment below and update the code to test analyticsEventPerDeviceCount
        //instance.analyticsEventPerDeviceCount(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsEventPerSessionCount', function() {
      it('should call analyticsEventPerSessionCount successfully', function(done) {
        //uncomment below and update the code to test analyticsEventPerSessionCount
        //instance.analyticsEventPerSessionCount(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsEventProperties', function() {
      it('should call analyticsEventProperties successfully', function(done) {
        //uncomment below and update the code to test analyticsEventProperties
        //instance.analyticsEventProperties(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsEventPropertyCounts', function() {
      it('should call analyticsEventPropertyCounts successfully', function(done) {
        //uncomment below and update the code to test analyticsEventPropertyCounts
        //instance.analyticsEventPropertyCounts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsEvents', function() {
      it('should call analyticsEvents successfully', function(done) {
        //uncomment below and update the code to test analyticsEvents
        //instance.analyticsEvents(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsEventsDelete', function() {
      it('should call analyticsEventsDelete successfully', function(done) {
        //uncomment below and update the code to test analyticsEventsDelete
        //instance.analyticsEventsDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsEventsDeleteLogs', function() {
      it('should call analyticsEventsDeleteLogs successfully', function(done) {
        //uncomment below and update the code to test analyticsEventsDeleteLogs
        //instance.analyticsEventsDeleteLogs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsGenericLogFlow', function() {
      it('should call analyticsGenericLogFlow successfully', function(done) {
        //uncomment below and update the code to test analyticsGenericLogFlow
        //instance.analyticsGenericLogFlow(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsGetAudience', function() {
      it('should call analyticsGetAudience successfully', function(done) {
        //uncomment below and update the code to test analyticsGetAudience
        //instance.analyticsGetAudience(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsLanguageCounts', function() {
      it('should call analyticsLanguageCounts successfully', function(done) {
        //uncomment below and update the code to test analyticsLanguageCounts
        //instance.analyticsLanguageCounts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsListAudiences', function() {
      it('should call analyticsListAudiences successfully', function(done) {
        //uncomment below and update the code to test analyticsListAudiences
        //instance.analyticsListAudiences(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsListCustomProperties', function() {
      it('should call analyticsListCustomProperties successfully', function(done) {
        //uncomment below and update the code to test analyticsListCustomProperties
        //instance.analyticsListCustomProperties(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsListDeviceProperties', function() {
      it('should call analyticsListDeviceProperties successfully', function(done) {
        //uncomment below and update the code to test analyticsListDeviceProperties
        //instance.analyticsListDeviceProperties(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsListDevicePropertyValues', function() {
      it('should call analyticsListDevicePropertyValues successfully', function(done) {
        //uncomment below and update the code to test analyticsListDevicePropertyValues
        //instance.analyticsListDevicePropertyValues(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsLogFlow', function() {
      it('should call analyticsLogFlow successfully', function(done) {
        //uncomment below and update the code to test analyticsLogFlow
        //instance.analyticsLogFlow(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsModelCounts', function() {
      it('should call analyticsModelCounts successfully', function(done) {
        //uncomment below and update the code to test analyticsModelCounts
        //instance.analyticsModelCounts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsOperatingSystemCounts', function() {
      it('should call analyticsOperatingSystemCounts successfully', function(done) {
        //uncomment below and update the code to test analyticsOperatingSystemCounts
        //instance.analyticsOperatingSystemCounts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsPerDeviceCounts', function() {
      it('should call analyticsPerDeviceCounts successfully', function(done) {
        //uncomment below and update the code to test analyticsPerDeviceCounts
        //instance.analyticsPerDeviceCounts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsPlaceCounts', function() {
      it('should call analyticsPlaceCounts successfully', function(done) {
        //uncomment below and update the code to test analyticsPlaceCounts
        //instance.analyticsPlaceCounts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsSessionCounts', function() {
      it('should call analyticsSessionCounts successfully', function(done) {
        //uncomment below and update the code to test analyticsSessionCounts
        //instance.analyticsSessionCounts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsSessionDurationsDistribution', function() {
      it('should call analyticsSessionDurationsDistribution successfully', function(done) {
        //uncomment below and update the code to test analyticsSessionDurationsDistribution
        //instance.analyticsSessionDurationsDistribution(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsTestAudience', function() {
      it('should call analyticsTestAudience successfully', function(done) {
        //uncomment below and update the code to test analyticsTestAudience
        //instance.analyticsTestAudience(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('analyticsVersions', function() {
      it('should call analyticsVersions successfully', function(done) {
        //uncomment below and update the code to test analyticsVersions
        //instance.analyticsVersions(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appBlockLogs', function() {
      it('should call appBlockLogs successfully', function(done) {
        //uncomment below and update the code to test appBlockLogs
        //instance.appBlockLogs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('crashesListSessionLogs', function() {
      it('should call crashesListSessionLogs successfully', function(done) {
        //uncomment below and update the code to test crashesListSessionLogs
        //instance.crashesListSessionLogs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('devicesBlockLogs', function() {
      it('should call devicesBlockLogs successfully', function(done) {
        //uncomment below and update the code to test devicesBlockLogs
        //instance.devicesBlockLogs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
