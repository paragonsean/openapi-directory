/**
 * Quick start - Telematics SDK
 * # Introduction We have prepared a set of APIs for quick start to integrate telematics SDK that powers mobile telematics inside 3rd party mobile applications.  * [CONTACT US](https://telematicssdk.com) * [SANDBOX](https://userdatahub.com) * [DEV.PORTAL](https://docs.telematicssdk.com) * [DEMO APP](https://raxeltelematics.com/telematics-app)   # Overview Datamotion provides telematics infrastructure for mobile applications.   Telematics SDK turns any smartphone into telematics data gathering device to collect Location, driving and behavior data. API services unlocks power of your mobile application  There are 3 groups of methods: * 1 - user management * 2 - statistics for mobile app * 3 - statistics for back-end(s)  in certain cases you will need SNS or any other notification services. read more [here](https://docs.telematicssdk.com/platform-features/sns) # Possible architecture  There are three common schemes that are used by our clients. These schemes can be combined * Collect, Process, Store (required: 1&2) * Collect, Process (required: 1& sns) * Collect (required 1&sns)   ## Collect, Process, Store ![Collect, Process, Store](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection%2C+processing%2C+storage)  ## Collect, Process ![Collect, Process](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection+and+processing)  ## Collect ![Collect](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection+only)  *** ![Telematic sdk](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Github/transportation_small.png)  # Common use-cases: * Safe and efficient driving * Usage-based insurance * Safe driving assessment * Driver assessment * Trip log * Geo-analysis * Accident monitoring * Driving engagements * Location based services * Realtime Tracking and beyond  # How to start * Register a [SANDBOX ACCOUNT](https://userdatahub.com) * Get [CREDENTIALS](https://docs.userdatahub.com/sandbox/credentials)  * Follow the guide from [DEVELOPER POERTAL](https://docs.telematicssdk.com)  # Authentication To create a user on datamotion platform, you require to use InstanceID and InstanceKEY. You can get it in Datahub -> management -> user-service credentials  Once you create a user, you will get Device token, JWT token and refresh token. then, you will use it for APIs
 *
 * The version of the OpenAPI document: 1.0.0
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
    factory(root.expect, root.QuickStartTelematicsSdk);
  }
}(this, function(expect, QuickStartTelematicsSdk) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new QuickStartTelematicsSdk.UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response();
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

  describe('UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response', function() {
    it('should create an instance of UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response', function() {
      // uncomment below and update the code to test UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response
      //var instance = new QuickStartTelematicsSdk.UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response();
      //expect(instance).to.be.a(QuickStartTelematicsSdk.UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response);
    });

    it('should have the property errors (base name: "Errors")', function() {
      // uncomment below and update the code to test the property errors
      //var instance = new QuickStartTelematicsSdk.UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response();
      //expect(instance).to.be();
    });

    it('should have the property result (base name: "Result")', function() {
      // uncomment below and update the code to test the property result
      //var instance = new QuickStartTelematicsSdk.UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "Status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new QuickStartTelematicsSdk.UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "Title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new QuickStartTelematicsSdk.UserSafeScoringDailyValueV1ScoringsIndividualDaily200Response();
      //expect(instance).to.be();
    });

  });

}));
