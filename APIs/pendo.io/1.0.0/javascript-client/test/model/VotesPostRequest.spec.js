/**
 * Pendo Feedback API
 * ## Who is this for?  This documentation is for developers creating their own integration with [Feedback's](https://www.pendo.io/product/feedback/) API. If you are doing a standard integration, there's a really easy [Javascript integration](https://help.receptive.io/hc/en-us/articles/209221969-How-to-integrate-Receptive-with-your-app) that you should know about before you go to the effort of building your own integration.  ## Authentication  API calls generally need to be authenticated. Generate an API Key at https://feedback.pendo.io/app/#/vendor/settings?section=integrate. This key should then be added to every request as a request header named 'auth-token' (preferred), or as a query parameter named 'auth-token'.  ## Endpoint  API endpoint is https://api.feedback.eu.pendo.io / https://api.feedback.us.pendo.io depending where your datacenter is located.  ## Notes  API endpoints are being added to this documentation as needed by customers. If you don't see an endpoint you need please contact support and if it exists we'll publish the docs here. The 'try it out' feature on this documentation page will probably be blocked by your browser because the Access-Control-Allow-Origin header has its value set by the Feedback server depending on your hostname.  ## Generating client code  This documentation is automatically generated from an OpenAPI spec available [here](http://apidoc.receptive.io/receptive.swagger.json). You can use Swagger to auto-generate API client code in many languages using the [Swagger Editor](http://editor.swagger.io/#/)
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@receptive.io
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
    factory(root.expect, root.PendoFeedbackApi);
  }
}(this, function(expect, PendoFeedbackApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new PendoFeedbackApi.VotesPostRequest();
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

  describe('VotesPostRequest', function() {
    it('should create an instance of VotesPostRequest', function() {
      // uncomment below and update the code to test VotesPostRequest
      //var instance = new PendoFeedbackApi.VotesPostRequest();
      //expect(instance).to.be.a(PendoFeedbackApi.VotesPostRequest);
    });

    it('should have the property userId (base name: "user_id")', function() {
      // uncomment below and update the code to test the property userId
      //var instance = new PendoFeedbackApi.VotesPostRequest();
      //expect(instance).to.be();
    });

    it('should have the property votes (base name: "votes")', function() {
      // uncomment below and update the code to test the property votes
      //var instance = new PendoFeedbackApi.VotesPostRequest();
      //expect(instance).to.be();
    });

  });

}));
