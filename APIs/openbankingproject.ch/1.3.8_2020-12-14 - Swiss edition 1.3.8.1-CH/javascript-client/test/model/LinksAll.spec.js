/**
 * Swiss NextGen Banking API-Framework
 * # Summary The **Swiss NextGen API** is based on the NextGenPSD2 *Framework Version 1.3.4* of the Berlin Group which offers a modern, open, harmonised and interoperable set of Application Programming Interfaces (APIs) as the safest and most efficient way to provide data securely. The NextGen Framework reduces XS2A complexity and costs, addresses the problem of multiple competing standards in Europe and, aligned with the goals of the Euro Retail Payments Board, enables European banking customers to benefit from innovative products and services ('Banking as a Service') by granting TPPs safe and secure (authenticated and authorised) access to their bank accounts and financial data.  The Swiss edtion refines the message formats specific to Switzerland and defines some matching examples.  The possible Approaches are:   * Redirect SCA Approach   * *(Not recommended by obp.ch community) OAuth SCA Approach*   * *(Not recommended by obp.ch community) Decoupled SCA Approach*   * *(Not recommended by obp.ch community) Embedded SCA Approach without SCA method*   * *(Not recommended by obp.ch community) Embedded SCA Approach with only one SCA method available*   * *(Not recommended by obp.ch community) Embedded SCA Approach with Selection of a SCA method*    Not every message defined in this API definition is necessary for all approaches.   Furthermore this API definition does not differ between methods which are mandatory, conditional, or optional   Therefore for a particular implementation of a compliant API it is only necessary to support   a certain subset of the methods defined in this API definition.    **Please have a look at the implementation guidelines if you are not sure   which message has to be used for the approach you are going to use.**  ## Some General Remarks Related to this version of the OpenAPI Specification: * **This API definition is based on the Implementation Guidelines of the [Berlin Group API](https://www.berlin-group.org/nextgenpsd2-downloads).**   It is not a replacement in any sense.   The main specification is (at the moment) always the Implementation Guidelines of the Berlin Group API. * **This API definition contains the REST-API for requests from the PISP to the ASPSP.** * **This API definition contains the messages for all different approaches defined in the Implementation Guidelines.** * According to the OpenAPI-Specification [https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md]      \"If in is \"header\" and the name field is \"Accept\", \"Content-Type\" or \"Authorization\", the parameter definition SHALL be ignored.\"    The element \"Accept\" will not be defined in this file at any place.    The elements \"Content-Type\" and \"Authorization\" are implicitly defined by the OpenApi tags \"content\" and \"security\".  * There are several predefined types which might occur in payment initiation messages,   but are not used in the standard JSON messages in the Implementation Guidelines.   Therefore they are not used in the corresponding messages in this file either.   We added them for the convenience of the user.   If there is a payment product, which needs these fields, one can easily use the predefined types.   But the ASPSP need not to accept them in general.  * **We omit the definition of all standard HTTP header elements (mandatory/optional/conditional)   except they are mentioned in the Implementation Guidelines.**   Therefore the implementer might add these in his own realisation of a comlient API in addition to the elements defined in this file.  ## General Remarks on Data Types  The Berlin Group definition of UTF-8 strings in context of the API have to support at least the following characters  a b c d e f g h i j k l m n o p q r s t u v w x y z  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  0 1 2 3 4 5 6 7 8 9  / - ? : ( ) . , ' +  Space 
 *
 * The version of the OpenAPI document: 1.3.8_2020-12-14 - Swiss edition 1.3.8.1-CH
 * Contact: info@obp.ch
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
    factory(root.expect, root.SwissNextGenBankingApiFramework);
  }
}(this, function(expect, SwissNextGenBankingApiFramework) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SwissNextGenBankingApiFramework.LinksAll();
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

  describe('LinksAll', function() {
    it('should create an instance of LinksAll', function() {
      // uncomment below and update the code to test LinksAll
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be.a(SwissNextGenBankingApiFramework.LinksAll);
    });

    it('should have the property account (base name: "account")', function() {
      // uncomment below and update the code to test the property account
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property authoriseTransaction (base name: "authoriseTransaction")', function() {
      // uncomment below and update the code to test the property authoriseTransaction
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property balances (base name: "balances")', function() {
      // uncomment below and update the code to test the property balances
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property cardAccount (base name: "cardAccount")', function() {
      // uncomment below and update the code to test the property cardAccount
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property cardTransactions (base name: "cardTransactions")', function() {
      // uncomment below and update the code to test the property cardTransactions
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property confirmation (base name: "confirmation")', function() {
      // uncomment below and update the code to test the property confirmation
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property download (base name: "download")', function() {
      // uncomment below and update the code to test the property download
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property first (base name: "first")', function() {
      // uncomment below and update the code to test the property first
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property last (base name: "last")', function() {
      // uncomment below and update the code to test the property last
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property next (base name: "next")', function() {
      // uncomment below and update the code to test the property next
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property previous (base name: "previous")', function() {
      // uncomment below and update the code to test the property previous
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property scaOAuth (base name: "scaOAuth")', function() {
      // uncomment below and update the code to test the property scaOAuth
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property scaRedirect (base name: "scaRedirect")', function() {
      // uncomment below and update the code to test the property scaRedirect
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property scaStatus (base name: "scaStatus")', function() {
      // uncomment below and update the code to test the property scaStatus
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property selectAuthenticationMethod (base name: "selectAuthenticationMethod")', function() {
      // uncomment below and update the code to test the property selectAuthenticationMethod
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property self (base name: "self")', function() {
      // uncomment below and update the code to test the property self
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property startAuthorisation (base name: "startAuthorisation")', function() {
      // uncomment below and update the code to test the property startAuthorisation
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property startAuthorisationWithAuthenticationMethodSelection (base name: "startAuthorisationWithAuthenticationMethodSelection")', function() {
      // uncomment below and update the code to test the property startAuthorisationWithAuthenticationMethodSelection
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property startAuthorisationWithEncryptedPsuAuthentication (base name: "startAuthorisationWithEncryptedPsuAuthentication")', function() {
      // uncomment below and update the code to test the property startAuthorisationWithEncryptedPsuAuthentication
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property startAuthorisationWithProprietaryData (base name: "startAuthorisationWithProprietaryData")', function() {
      // uncomment below and update the code to test the property startAuthorisationWithProprietaryData
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property startAuthorisationWithPsuAuthentication (base name: "startAuthorisationWithPsuAuthentication")', function() {
      // uncomment below and update the code to test the property startAuthorisationWithPsuAuthentication
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property startAuthorisationWithPsuIdentification (base name: "startAuthorisationWithPsuIdentification")', function() {
      // uncomment below and update the code to test the property startAuthorisationWithPsuIdentification
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property startAuthorisationWithTransactionAuthorisation (base name: "startAuthorisationWithTransactionAuthorisation")', function() {
      // uncomment below and update the code to test the property startAuthorisationWithTransactionAuthorisation
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property transactionDetails (base name: "transactionDetails")', function() {
      // uncomment below and update the code to test the property transactionDetails
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property transactions (base name: "transactions")', function() {
      // uncomment below and update the code to test the property transactions
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property updateAdditionalEncryptedPsuAuthentication (base name: "updateAdditionalEncryptedPsuAuthentication")', function() {
      // uncomment below and update the code to test the property updateAdditionalEncryptedPsuAuthentication
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property updateAdditionalPsuAuthentication (base name: "updateAdditionalPsuAuthentication")', function() {
      // uncomment below and update the code to test the property updateAdditionalPsuAuthentication
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property updateEncryptedPsuAuthentication (base name: "updateEncryptedPsuAuthentication")', function() {
      // uncomment below and update the code to test the property updateEncryptedPsuAuthentication
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property updateProprietaryData (base name: "updateProprietaryData")', function() {
      // uncomment below and update the code to test the property updateProprietaryData
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property updatePsuAuthentication (base name: "updatePsuAuthentication")', function() {
      // uncomment below and update the code to test the property updatePsuAuthentication
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

    it('should have the property updatePsuIdentification (base name: "updatePsuIdentification")', function() {
      // uncomment below and update the code to test the property updatePsuIdentification
      //var instance = new SwissNextGenBankingApiFramework.LinksAll();
      //expect(instance).to.be();
    });

  });

}));
