/**
 * PAC Control REST API
 * #### Revised: 6/15/2018  ### Overview This API provides secure access to a SNAP-PAC-R or -S series controller's variable and I/O tags. Confidentiality for API transactions is provided by HTTPS. Authentication uses HTTP Basic Authentication with an API key. An API key ID is submitted in the Basic Authentication userid field and API key value in the password field.  **For more information visit:** [developer.opto22.com](http://developer.opto22.com)  ### Examples  **Read an array** of all the integer32 variables defined in the PAC's strategy. For example, on your SNAP-PAC-R or -S series controller at IP address 1.2.3.4, you would use the URL:   ``` https://1.2.3.4/api/v1/device/strategy/vars/int32s ``` and provide appropriate authentication. The GET response will be a JSON array of name-value  pairs such as:  ```json [ { \"nMyVeryFavoriteNumber\": 22 },   { \"nWidgetsProducedToday\": 22222 },   { \"DELAY_LOOP_TIME_IN_MSECS\"  : 200 } ] ``` **Read the engineering units** (EU) of an analog input point configured in the PAC's strategy. For an analog input (I/O point) named aiTemperatureInDegreesF, use   `https://1.2.3.4/api/v1/device/strategy/ios/analogInputs/aiTemperatureInDegreesF/eu`  The GET response will be a single JSON name-value pair such as: ```json { \"value\": 72.22 } ```      ### Note on packet sizes: When doing POSTs or GETs, the JSON payload in the body should not exceed 3k (3072 bytes). 
 *
 * The version of the OpenAPI document: R1.0a
 * Contact: developer@opto22.com
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
    factory(root.expect, root.PacControlRestApi);
  }
}(this, function(expect, PacControlRestApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new PacControlRestApi.AllApi();
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

  describe('AllApi', function() {
    describe('readAnalogInputEu', function() {
      it('should call readAnalogInputEu successfully', function(done) {
        //uncomment below and update the code to test readAnalogInputEu
        //instance.readAnalogInputEu(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readAnalogInputs', function() {
      it('should call readAnalogInputs successfully', function(done) {
        //uncomment below and update the code to test readAnalogInputs
        //instance.readAnalogInputs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readAnalogOutputEu', function() {
      it('should call readAnalogOutputEu successfully', function(done) {
        //uncomment below and update the code to test readAnalogOutputEu
        //instance.readAnalogOutputEu(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readAnalogOutputs', function() {
      it('should call readAnalogOutputs successfully', function(done) {
        //uncomment below and update the code to test readAnalogOutputs
        //instance.readAnalogOutputs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readDeviceDetails', function() {
      it('should call readDeviceDetails successfully', function(done) {
        //uncomment below and update the code to test readDeviceDetails
        //instance.readDeviceDetails(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readDigitalInputState', function() {
      it('should call readDigitalInputState successfully', function(done) {
        //uncomment below and update the code to test readDigitalInputState
        //instance.readDigitalInputState(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readDigitalInputs', function() {
      it('should call readDigitalInputs successfully', function(done) {
        //uncomment below and update the code to test readDigitalInputs
        //instance.readDigitalInputs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readDigitalOutputState', function() {
      it('should call readDigitalOutputState successfully', function(done) {
        //uncomment below and update the code to test readDigitalOutputState
        //instance.readDigitalOutputState(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readDigitalOutputs', function() {
      it('should call readDigitalOutputs successfully', function(done) {
        //uncomment below and update the code to test readDigitalOutputs
        //instance.readDigitalOutputs(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readDownTimerValue', function() {
      it('should call readDownTimerValue successfully', function(done) {
        //uncomment below and update the code to test readDownTimerValue
        //instance.readDownTimerValue(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readDownTimerVars', function() {
      it('should call readDownTimerVars successfully', function(done) {
        //uncomment below and update the code to test readDownTimerVars
        //instance.readDownTimerVars(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readFloatTable', function() {
      it('should call readFloatTable successfully', function(done) {
        //uncomment below and update the code to test readFloatTable
        //instance.readFloatTable(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readFloatTableElement', function() {
      it('should call readFloatTableElement successfully', function(done) {
        //uncomment below and update the code to test readFloatTableElement
        //instance.readFloatTableElement(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readFloatTables', function() {
      it('should call readFloatTables successfully', function(done) {
        //uncomment below and update the code to test readFloatTables
        //instance.readFloatTables(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readFloatVar', function() {
      it('should call readFloatVar successfully', function(done) {
        //uncomment below and update the code to test readFloatVar
        //instance.readFloatVar(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readFloatVars', function() {
      it('should call readFloatVars successfully', function(done) {
        //uncomment below and update the code to test readFloatVars
        //instance.readFloatVars(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readInt32Table', function() {
      it('should call readInt32Table successfully', function(done) {
        //uncomment below and update the code to test readInt32Table
        //instance.readInt32Table(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readInt32TableElement', function() {
      it('should call readInt32TableElement successfully', function(done) {
        //uncomment below and update the code to test readInt32TableElement
        //instance.readInt32TableElement(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readInt32Tables', function() {
      it('should call readInt32Tables successfully', function(done) {
        //uncomment below and update the code to test readInt32Tables
        //instance.readInt32Tables(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readInt32Var', function() {
      it('should call readInt32Var successfully', function(done) {
        //uncomment below and update the code to test readInt32Var
        //instance.readInt32Var(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readInt32Vars', function() {
      it('should call readInt32Vars successfully', function(done) {
        //uncomment below and update the code to test readInt32Vars
        //instance.readInt32Vars(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readInt64Table', function() {
      it('should call readInt64Table successfully', function(done) {
        //uncomment below and update the code to test readInt64Table
        //instance.readInt64Table(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readInt64TableAsString', function() {
      it('should call readInt64TableAsString successfully', function(done) {
        //uncomment below and update the code to test readInt64TableAsString
        //instance.readInt64TableAsString(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readInt64TableElement', function() {
      it('should call readInt64TableElement successfully', function(done) {
        //uncomment below and update the code to test readInt64TableElement
        //instance.readInt64TableElement(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readInt64TableElementAsString', function() {
      it('should call readInt64TableElementAsString successfully', function(done) {
        //uncomment below and update the code to test readInt64TableElementAsString
        //instance.readInt64TableElementAsString(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readInt64Tables', function() {
      it('should call readInt64Tables successfully', function(done) {
        //uncomment below and update the code to test readInt64Tables
        //instance.readInt64Tables(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readInt64Var', function() {
      it('should call readInt64Var successfully', function(done) {
        //uncomment below and update the code to test readInt64Var
        //instance.readInt64Var(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readInt64VarAsString', function() {
      it('should call readInt64VarAsString successfully', function(done) {
        //uncomment below and update the code to test readInt64VarAsString
        //instance.readInt64VarAsString(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readInt64Vars', function() {
      it('should call readInt64Vars successfully', function(done) {
        //uncomment below and update the code to test readInt64Vars
        //instance.readInt64Vars(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readInt64VarsAsStrings', function() {
      it('should call readInt64VarsAsStrings successfully', function(done) {
        //uncomment below and update the code to test readInt64VarsAsStrings
        //instance.readInt64VarsAsStrings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readStrategyDetails', function() {
      it('should call readStrategyDetails successfully', function(done) {
        //uncomment below and update the code to test readStrategyDetails
        //instance.readStrategyDetails(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readStringTable', function() {
      it('should call readStringTable successfully', function(done) {
        //uncomment below and update the code to test readStringTable
        //instance.readStringTable(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readStringTableElement', function() {
      it('should call readStringTableElement successfully', function(done) {
        //uncomment below and update the code to test readStringTableElement
        //instance.readStringTableElement(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readStringTables', function() {
      it('should call readStringTables successfully', function(done) {
        //uncomment below and update the code to test readStringTables
        //instance.readStringTables(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readStringVar', function() {
      it('should call readStringVar successfully', function(done) {
        //uncomment below and update the code to test readStringVar
        //instance.readStringVar(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readStringVars', function() {
      it('should call readStringVars successfully', function(done) {
        //uncomment below and update the code to test readStringVars
        //instance.readStringVars(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readUpTimerValue', function() {
      it('should call readUpTimerValue successfully', function(done) {
        //uncomment below and update the code to test readUpTimerValue
        //instance.readUpTimerValue(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('readUpTimerVars', function() {
      it('should call readUpTimerVars successfully', function(done) {
        //uncomment below and update the code to test readUpTimerVars
        //instance.readUpTimerVars(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeAnalogOutputEu', function() {
      it('should call writeAnalogOutputEu successfully', function(done) {
        //uncomment below and update the code to test writeAnalogOutputEu
        //instance.writeAnalogOutputEu(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeDigitalOutputState', function() {
      it('should call writeDigitalOutputState successfully', function(done) {
        //uncomment below and update the code to test writeDigitalOutputState
        //instance.writeDigitalOutputState(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeFloatTable', function() {
      it('should call writeFloatTable successfully', function(done) {
        //uncomment below and update the code to test writeFloatTable
        //instance.writeFloatTable(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeFloatTableElement', function() {
      it('should call writeFloatTableElement successfully', function(done) {
        //uncomment below and update the code to test writeFloatTableElement
        //instance.writeFloatTableElement(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeFloatVar', function() {
      it('should call writeFloatVar successfully', function(done) {
        //uncomment below and update the code to test writeFloatVar
        //instance.writeFloatVar(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeInt32Table', function() {
      it('should call writeInt32Table successfully', function(done) {
        //uncomment below and update the code to test writeInt32Table
        //instance.writeInt32Table(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeInt32TableElement', function() {
      it('should call writeInt32TableElement successfully', function(done) {
        //uncomment below and update the code to test writeInt32TableElement
        //instance.writeInt32TableElement(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeInt32Var', function() {
      it('should call writeInt32Var successfully', function(done) {
        //uncomment below and update the code to test writeInt32Var
        //instance.writeInt32Var(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeInt64Table', function() {
      it('should call writeInt64Table successfully', function(done) {
        //uncomment below and update the code to test writeInt64Table
        //instance.writeInt64Table(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeInt64TableAsString', function() {
      it('should call writeInt64TableAsString successfully', function(done) {
        //uncomment below and update the code to test writeInt64TableAsString
        //instance.writeInt64TableAsString(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeInt64TableElement', function() {
      it('should call writeInt64TableElement successfully', function(done) {
        //uncomment below and update the code to test writeInt64TableElement
        //instance.writeInt64TableElement(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeInt64TableElementAsString', function() {
      it('should call writeInt64TableElementAsString successfully', function(done) {
        //uncomment below and update the code to test writeInt64TableElementAsString
        //instance.writeInt64TableElementAsString(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeInt64Var', function() {
      it('should call writeInt64Var successfully', function(done) {
        //uncomment below and update the code to test writeInt64Var
        //instance.writeInt64Var(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeInt64VarAsString', function() {
      it('should call writeInt64VarAsString successfully', function(done) {
        //uncomment below and update the code to test writeInt64VarAsString
        //instance.writeInt64VarAsString(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeStringTable', function() {
      it('should call writeStringTable successfully', function(done) {
        //uncomment below and update the code to test writeStringTable
        //instance.writeStringTable(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeStringTableElement', function() {
      it('should call writeStringTableElement successfully', function(done) {
        //uncomment below and update the code to test writeStringTableElement
        //instance.writeStringTableElement(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('writeStringVar', function() {
      it('should call writeStringVar successfully', function(done) {
        //uncomment below and update the code to test writeStringVar
        //instance.writeStringVar(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
