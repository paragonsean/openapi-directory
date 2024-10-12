/**
 * EmailVerify
 * OTP email verification API by PayPI. <br/><br/> EmailVerify provides a simple way to verify email addresses. We send emails ourselves taking the burden of setting up email systems and tracking codes. <br/><br/> To learn more about this API, check out [EmailVerify documentation](https://emailverify.paypi.dev/) <br/><br/>  ## Authentication All requests to the EmailVerify API must be authenticated with an API Key. To get an API key, subscribe to the EmailVerify [here](https://app.paypi.dev/subscribe/c2VydmljZTo1OGQxZDNmMy05OWQ5LTQ3ZjYtOWJkNi02OWNkMTY1OGFmOWU=).  \\ Set your `Authorization` header to `Bearer YOUR-API-KEY`.  ``` curl -H \"Content-Type: application/json\" \\ -H \"Authorization: Bearer YOUR-API-KEY\" \\ ... ``` 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: hello@paypi.dev
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
    factory(root.expect, root.EmailVerify);
  }
}(this, function(expect, EmailVerify) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new EmailVerify.SendCodePostRequest();
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

  describe('SendCodePostRequest', function() {
    it('should create an instance of SendCodePostRequest', function() {
      // uncomment below and update the code to test SendCodePostRequest
      //var instance = new EmailVerify.SendCodePostRequest();
      //expect(instance).to.be.a(EmailVerify.SendCodePostRequest);
    });

    it('should have the property email (base name: "email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new EmailVerify.SendCodePostRequest();
      //expect(instance).to.be();
    });

  });

}));
