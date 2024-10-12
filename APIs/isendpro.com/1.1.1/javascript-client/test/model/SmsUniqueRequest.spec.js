/**
 * API iSendPro
 * [1] Liste des fonctionnalités : - envoi de SMS à un ou plusieurs destinataires, - lookup HLR, - récupération des récapitulatifs de campagne, - gestion des répertoires, - ajout en liste noire. - comptage du nombre de caractères des SMS  [2] Pour utiliser cette API vous devez: - Créer un compte iSendPro sur https://isendpro.com/ - Créditer votre compte      - Remarque: obtention d'un crédit de test possible sous conditions - Noter votre clé de compte (keyid)   - Elle vous sera indispensable à l'utilisation de l'API   - Vous pouvez la trouver dans le rubrique mon \"compte\", sous-rubrique \"mon API\" - Configurer le contrôle IP   - Le contrôle IP est configurable dans le rubrique mon \"compte\", sous-rubrique \"mon API\"   - Il s'agit d'un système de liste blanche, vous devez entrer les IP utilisées pour appeler l'API   - Vous pouvez également désactiver totalement le contrôle IP 
 *
 * The version of the OpenAPI document: 1.1.1
 * Contact: support@isendpro.com
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
    factory(root.expect, root.ApiISendPro);
  }
}(this, function(expect, ApiISendPro) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ApiISendPro.SmsUniqueRequest();
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

  describe('SmsUniqueRequest', function() {
    it('should create an instance of SmsUniqueRequest', function() {
      // uncomment below and update the code to test SmsUniqueRequest
      //var instance = new ApiISendPro.SmsUniqueRequest();
      //expect(instance).to.be.a(ApiISendPro.SmsUniqueRequest);
    });

    it('should have the property dateEnvoi (base name: "date_envoi")', function() {
      // uncomment below and update the code to test the property dateEnvoi
      //var instance = new ApiISendPro.SmsUniqueRequest();
      //expect(instance).to.be();
    });

    it('should have the property emetteur (base name: "emetteur")', function() {
      // uncomment below and update the code to test the property emetteur
      //var instance = new ApiISendPro.SmsUniqueRequest();
      //expect(instance).to.be();
    });

    it('should have the property gmtZone (base name: "gmt_zone")', function() {
      // uncomment below and update the code to test the property gmtZone
      //var instance = new ApiISendPro.SmsUniqueRequest();
      //expect(instance).to.be();
    });

    it('should have the property keyid (base name: "keyid")', function() {
      // uncomment below and update the code to test the property keyid
      //var instance = new ApiISendPro.SmsUniqueRequest();
      //expect(instance).to.be();
    });

    it('should have the property nostop (base name: "nostop")', function() {
      // uncomment below and update the code to test the property nostop
      //var instance = new ApiISendPro.SmsUniqueRequest();
      //expect(instance).to.be();
    });

    it('should have the property num (base name: "num")', function() {
      // uncomment below and update the code to test the property num
      //var instance = new ApiISendPro.SmsUniqueRequest();
      //expect(instance).to.be();
    });

    it('should have the property numAzur (base name: "numAzur")', function() {
      // uncomment below and update the code to test the property numAzur
      //var instance = new ApiISendPro.SmsUniqueRequest();
      //expect(instance).to.be();
    });

    it('should have the property sms (base name: "sms")', function() {
      // uncomment below and update the code to test the property sms
      //var instance = new ApiISendPro.SmsUniqueRequest();
      //expect(instance).to.be();
    });

    it('should have the property smslong (base name: "smslong")', function() {
      // uncomment below and update the code to test the property smslong
      //var instance = new ApiISendPro.SmsUniqueRequest();
      //expect(instance).to.be();
    });

    it('should have the property tracker (base name: "tracker")', function() {
      // uncomment below and update the code to test the property tracker
      //var instance = new ApiISendPro.SmsUniqueRequest();
      //expect(instance).to.be();
    });

    it('should have the property ucs2 (base name: "ucs2")', function() {
      // uncomment below and update the code to test the property ucs2
      //var instance = new ApiISendPro.SmsUniqueRequest();
      //expect(instance).to.be();
    });

  });

}));
