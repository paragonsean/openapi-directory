/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
    factory(root.expect, root.MagentoB2B);
  }
}(this, function(expect, MagentoB2B) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MagentoB2B.SalesDataOrderPaymentInterface();
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

  describe('SalesDataOrderPaymentInterface', function() {
    it('should create an instance of SalesDataOrderPaymentInterface', function() {
      // uncomment below and update the code to test SalesDataOrderPaymentInterface
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be.a(MagentoB2B.SalesDataOrderPaymentInterface);
    });

    it('should have the property accountStatus (base name: "account_status")', function() {
      // uncomment below and update the code to test the property accountStatus
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property additionalData (base name: "additional_data")', function() {
      // uncomment below and update the code to test the property additionalData
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property additionalInformation (base name: "additional_information")', function() {
      // uncomment below and update the code to test the property additionalInformation
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property addressStatus (base name: "address_status")', function() {
      // uncomment below and update the code to test the property addressStatus
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property amountAuthorized (base name: "amount_authorized")', function() {
      // uncomment below and update the code to test the property amountAuthorized
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property amountCanceled (base name: "amount_canceled")', function() {
      // uncomment below and update the code to test the property amountCanceled
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property amountOrdered (base name: "amount_ordered")', function() {
      // uncomment below and update the code to test the property amountOrdered
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property amountPaid (base name: "amount_paid")', function() {
      // uncomment below and update the code to test the property amountPaid
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property amountRefunded (base name: "amount_refunded")', function() {
      // uncomment below and update the code to test the property amountRefunded
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property anetTransMethod (base name: "anet_trans_method")', function() {
      // uncomment below and update the code to test the property anetTransMethod
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property baseAmountAuthorized (base name: "base_amount_authorized")', function() {
      // uncomment below and update the code to test the property baseAmountAuthorized
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property baseAmountCanceled (base name: "base_amount_canceled")', function() {
      // uncomment below and update the code to test the property baseAmountCanceled
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property baseAmountOrdered (base name: "base_amount_ordered")', function() {
      // uncomment below and update the code to test the property baseAmountOrdered
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property baseAmountPaid (base name: "base_amount_paid")', function() {
      // uncomment below and update the code to test the property baseAmountPaid
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property baseAmountPaidOnline (base name: "base_amount_paid_online")', function() {
      // uncomment below and update the code to test the property baseAmountPaidOnline
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property baseAmountRefunded (base name: "base_amount_refunded")', function() {
      // uncomment below and update the code to test the property baseAmountRefunded
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property baseAmountRefundedOnline (base name: "base_amount_refunded_online")', function() {
      // uncomment below and update the code to test the property baseAmountRefundedOnline
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property baseShippingAmount (base name: "base_shipping_amount")', function() {
      // uncomment below and update the code to test the property baseShippingAmount
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property baseShippingCaptured (base name: "base_shipping_captured")', function() {
      // uncomment below and update the code to test the property baseShippingCaptured
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property baseShippingRefunded (base name: "base_shipping_refunded")', function() {
      // uncomment below and update the code to test the property baseShippingRefunded
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccApproval (base name: "cc_approval")', function() {
      // uncomment below and update the code to test the property ccApproval
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccAvsStatus (base name: "cc_avs_status")', function() {
      // uncomment below and update the code to test the property ccAvsStatus
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccCidStatus (base name: "cc_cid_status")', function() {
      // uncomment below and update the code to test the property ccCidStatus
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccDebugRequestBody (base name: "cc_debug_request_body")', function() {
      // uncomment below and update the code to test the property ccDebugRequestBody
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccDebugResponseBody (base name: "cc_debug_response_body")', function() {
      // uncomment below and update the code to test the property ccDebugResponseBody
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccDebugResponseSerialized (base name: "cc_debug_response_serialized")', function() {
      // uncomment below and update the code to test the property ccDebugResponseSerialized
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccExpMonth (base name: "cc_exp_month")', function() {
      // uncomment below and update the code to test the property ccExpMonth
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccExpYear (base name: "cc_exp_year")', function() {
      // uncomment below and update the code to test the property ccExpYear
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccLast4 (base name: "cc_last4")', function() {
      // uncomment below and update the code to test the property ccLast4
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccNumberEnc (base name: "cc_number_enc")', function() {
      // uncomment below and update the code to test the property ccNumberEnc
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccOwner (base name: "cc_owner")', function() {
      // uncomment below and update the code to test the property ccOwner
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccSecureVerify (base name: "cc_secure_verify")', function() {
      // uncomment below and update the code to test the property ccSecureVerify
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccSsIssue (base name: "cc_ss_issue")', function() {
      // uncomment below and update the code to test the property ccSsIssue
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccSsStartMonth (base name: "cc_ss_start_month")', function() {
      // uncomment below and update the code to test the property ccSsStartMonth
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccSsStartYear (base name: "cc_ss_start_year")', function() {
      // uncomment below and update the code to test the property ccSsStartYear
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccStatus (base name: "cc_status")', function() {
      // uncomment below and update the code to test the property ccStatus
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccStatusDescription (base name: "cc_status_description")', function() {
      // uncomment below and update the code to test the property ccStatusDescription
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccTransId (base name: "cc_trans_id")', function() {
      // uncomment below and update the code to test the property ccTransId
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property ccType (base name: "cc_type")', function() {
      // uncomment below and update the code to test the property ccType
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property echeckAccountName (base name: "echeck_account_name")', function() {
      // uncomment below and update the code to test the property echeckAccountName
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property echeckAccountType (base name: "echeck_account_type")', function() {
      // uncomment below and update the code to test the property echeckAccountType
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property echeckBankName (base name: "echeck_bank_name")', function() {
      // uncomment below and update the code to test the property echeckBankName
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property echeckRoutingNumber (base name: "echeck_routing_number")', function() {
      // uncomment below and update the code to test the property echeckRoutingNumber
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property echeckType (base name: "echeck_type")', function() {
      // uncomment below and update the code to test the property echeckType
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property entityId (base name: "entity_id")', function() {
      // uncomment below and update the code to test the property entityId
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property extensionAttributes (base name: "extension_attributes")', function() {
      // uncomment below and update the code to test the property extensionAttributes
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property lastTransId (base name: "last_trans_id")', function() {
      // uncomment below and update the code to test the property lastTransId
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property method (base name: "method")', function() {
      // uncomment below and update the code to test the property method
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property parentId (base name: "parent_id")', function() {
      // uncomment below and update the code to test the property parentId
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property poNumber (base name: "po_number")', function() {
      // uncomment below and update the code to test the property poNumber
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property protectionEligibility (base name: "protection_eligibility")', function() {
      // uncomment below and update the code to test the property protectionEligibility
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property quotePaymentId (base name: "quote_payment_id")', function() {
      // uncomment below and update the code to test the property quotePaymentId
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property shippingAmount (base name: "shipping_amount")', function() {
      // uncomment below and update the code to test the property shippingAmount
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property shippingCaptured (base name: "shipping_captured")', function() {
      // uncomment below and update the code to test the property shippingCaptured
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

    it('should have the property shippingRefunded (base name: "shipping_refunded")', function() {
      // uncomment below and update the code to test the property shippingRefunded
      //var instance = new MagentoB2B.SalesDataOrderPaymentInterface();
      //expect(instance).to.be();
    });

  });

}));
