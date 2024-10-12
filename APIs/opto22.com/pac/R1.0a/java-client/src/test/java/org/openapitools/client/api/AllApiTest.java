/*
 * PAC Control REST API
 * #### Revised: 6/15/2018  ### Overview This API provides secure access to a SNAP-PAC-R or -S series controller's variable and I/O tags. Confidentiality for API transactions is provided by HTTPS. Authentication uses HTTP Basic Authentication with an API key. An API key ID is submitted in the Basic Authentication userid field and API key value in the password field.  **For more information visit:** [developer.opto22.com](http://developer.opto22.com)  ### Examples  **Read an array** of all the integer32 variables defined in the PAC's strategy. For example, on your SNAP-PAC-R or -S series controller at IP address 1.2.3.4, you would use the URL:   ``` https://1.2.3.4/api/v1/device/strategy/vars/int32s ``` and provide appropriate authentication. The GET response will be a JSON array of name-value  pairs such as:  ```json [ { \"nMyVeryFavoriteNumber\": 22 },   { \"nWidgetsProducedToday\": 22222 },   { \"DELAY_LOOP_TIME_IN_MSECS\"  : 200 } ] ``` **Read the engineering units** (EU) of an analog input point configured in the PAC's strategy. For an analog input (I/O point) named aiTemperatureInDegreesF, use   `https://1.2.3.4/api/v1/device/strategy/ios/analogInputs/aiTemperatureInDegreesF/eu`  The GET response will be a single JSON name-value pair such as: ```json { \"value\": 72.22 } ```      ### Note on packet sizes: When doing POSTs or GETs, the JSON payload in the body should not exceed 3k (3072 bytes). 
 *
 * The version of the OpenAPI document: R1.0a
 * Contact: developer@opto22.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ControllerResponse;
import org.openapitools.client.model.DigitalPointStateObject;
import org.openapitools.client.model.DigitalPointStateVar;
import org.openapitools.client.model.ErrorResponse200OKish;
import org.openapitools.client.model.ErrorResponse400BadAdminOrValue;
import org.openapitools.client.model.ErrorResponse401BadKeyForBasicAuth;
import org.openapitools.client.model.ErrorResponse404NotFound;
import org.openapitools.client.model.FloatValueObject;
import org.openapitools.client.model.FloatVar;
import org.openapitools.client.model.Int32ValueObject;
import org.openapitools.client.model.Int32Var;
import org.openapitools.client.model.Int64StringValueObject;
import org.openapitools.client.model.Int64ValueObject;
import org.openapitools.client.model.Int64Var;
import org.openapitools.client.model.Int64VarAsString;
import org.openapitools.client.model.StrategyResponse;
import org.openapitools.client.model.StringValueObject;
import org.openapitools.client.model.StringVar;
import org.openapitools.client.model.TableDef;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AllApi
 */
@Disabled
public class AllApiTest {

    private final AllApi api = new AllApi();

    /**
     * Reads the value in engineering units (EU) of the specified analog input
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readAnalogInputEuTest() throws ApiException {
        String ioName = null;
        FloatValueObject response = api.readAnalogInputEu(ioName);
        // TODO: test validations
    }

    /**
     * Returns the name and engineering units (EU) for all analog input points in the strategy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readAnalogInputsTest() throws ApiException {
        List<FloatVar> response = api.readAnalogInputs();
        // TODO: test validations
    }

    /**
     * Reads the value in engineering units (EU) of the specified analog output
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readAnalogOutputEuTest() throws ApiException {
        String ioName = null;
        FloatValueObject response = api.readAnalogOutputEu(ioName);
        // TODO: test validations
    }

    /**
     * Returns the name and engineering units (EU) for all analog output points in the strategy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readAnalogOutputsTest() throws ApiException {
        List<FloatVar> response = api.readAnalogOutputs();
        // TODO: test validations
    }

    /**
     * Returns controller&#39;s type; firmware version; both mac addresses; and uptime in seconds
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readDeviceDetailsTest() throws ApiException {
        ControllerResponse response = api.readDeviceDetails();
        // TODO: test validations
    }

    /**
     * Returns the specified digital input point&#39;s state (true &#x3D; on, false &#x3D; off)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readDigitalInputStateTest() throws ApiException {
        String ioName = null;
        DigitalPointStateObject response = api.readDigitalInputState(ioName);
        // TODO: test validations
    }

    /**
     * Returns the name and state (true &#x3D; on, false &#x3D; off) of all digital input points in the strategy. If there is no strategy in the controller, or the strategy includes no digital inputs, the returned array will be empty.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readDigitalInputsTest() throws ApiException {
        List<DigitalPointStateVar> response = api.readDigitalInputs();
        // TODO: test validations
    }

    /**
     * Returns the specified digital output point&#39;s state (true &#x3D; on, false &#x3D; off)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readDigitalOutputStateTest() throws ApiException {
        String ioName = null;
        DigitalPointStateObject response = api.readDigitalOutputState(ioName);
        // TODO: test validations
    }

    /**
     * Returns the name and state (true &#x3D; on, false &#x3D; off) of all digital output points in the strategy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readDigitalOutputsTest() throws ApiException {
        List<DigitalPointStateVar> response = api.readDigitalOutputs();
        // TODO: test validations
    }

    /**
     * Returns current value of the specified down timer
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readDownTimerValueTest() throws ApiException {
        String downTimerName = null;
        FloatValueObject response = api.readDownTimerValue(downTimerName);
        // TODO: test validations
    }

    /**
     * Returns the name and current value of all down timers in the strategy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readDownTimerVarsTest() throws ApiException {
        List<FloatVar> response = api.readDownTimerVars();
        // TODO: test validations
    }

    /**
     * Read table elements #### Examples #### * Read all elements in a table named ftable: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable * Read elements 5 and up in a table named ftable starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;5 * Read 3 consecutive elements in a table named ftable starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;10&amp;numElements&#x3D;3 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readFloatTableTest() throws ApiException {
        String tableName = null;
        Integer startIndex = null;
        Integer numElements = null;
        List<Float> response = api.readFloatTable(tableName, startIndex, numElements);
        // TODO: test validations
    }

    /**
     * Read specified table element
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readFloatTableElementTest() throws ApiException {
        String tableName = null;
        Integer index = null;
        FloatValueObject response = api.readFloatTableElement(tableName, index);
        // TODO: test validations
    }

    /**
     * Returns an array of the name and length of all the float tables in the strategy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readFloatTablesTest() throws ApiException {
        List<TableDef> response = api.readFloatTables();
        // TODO: test validations
    }

    /**
     * Returns value of the specified float variable
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readFloatVarTest() throws ApiException {
        String floatName = null;
        FloatValueObject response = api.readFloatVar(floatName);
        // TODO: test validations
    }

    /**
     * Returns the name and value of all (single-precision) float variables in the strategy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readFloatVarsTest() throws ApiException {
        List<FloatVar> response = api.readFloatVars();
        // TODO: test validations
    }

    /**
     * \&quot;Read a range of table elements from the specified integer32 table\&quot;  #### Examples ####  * Read all elements in a table named itable: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable  * Read elements 5 and up in a table named itable starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;5  * Read 3 consecutive elements in a table named itable starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;10&amp;numElements&#x3D;3 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readInt32TableTest() throws ApiException {
        String tableName = null;
        Integer startIndex = null;
        Integer numElements = null;
        List<Integer> response = api.readInt32Table(tableName, startIndex, numElements);
        // TODO: test validations
    }

    /**
     * Read specified integer32 table element
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readInt32TableElementTest() throws ApiException {
        String tableName = null;
        Integer index = null;
        Int32ValueObject response = api.readInt32TableElement(tableName, index);
        // TODO: test validations
    }

    /**
     * Returns an array of the name and length of all the integer32 tables in the strategy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readInt32TablesTest() throws ApiException {
        List<TableDef> response = api.readInt32Tables();
        // TODO: test validations
    }

    /**
     * Returns value of the specified integer32 variable
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readInt32VarTest() throws ApiException {
        String int32Name = null;
        Int32ValueObject response = api.readInt32Var(int32Name);
        // TODO: test validations
    }

    /**
     * Returns the name and value of all integer32 variables in the strategy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readInt32VarsTest() throws ApiException {
        List<Int32Var> response = api.readInt32Vars();
        // TODO: test validations
    }

    /**
     * \&quot;Read a range of table elements from the specified integer64 table\&quot;  #### Examples ####  * Read all elements in a table named i64table: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;10&amp;numElements&#x3D;3 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readInt64TableTest() throws ApiException {
        String tableName = null;
        Integer startIndex = null;
        Integer numElements = null;
        List<Long> response = api.readInt64Table(tableName, startIndex, numElements);
        // TODO: test validations
    }

    /**
     * \&quot;Read a range of table elements from the specified integer64 table\&quot;  #### Examples ####  * Read all elements in a table named i64table: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;10&amp;numElements&#x3D;3 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readInt64TableAsStringTest() throws ApiException {
        String tableName = null;
        Integer startIndex = null;
        Integer numElements = null;
        List<String> response = api.readInt64TableAsString(tableName, startIndex, numElements);
        // TODO: test validations
    }

    /**
     * Read specified integer64 table element
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readInt64TableElementTest() throws ApiException {
        String tableName = null;
        Integer index = null;
        Int64ValueObject response = api.readInt64TableElement(tableName, index);
        // TODO: test validations
    }

    /**
     * Read specified integer64 table element as string
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readInt64TableElementAsStringTest() throws ApiException {
        String tableName = null;
        Integer index = null;
        Int64StringValueObject response = api.readInt64TableElementAsString(tableName, index);
        // TODO: test validations
    }

    /**
     * Returns an array of the name and length of all the integer64 tables in the strategy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readInt64TablesTest() throws ApiException {
        List<TableDef> response = api.readInt64Tables();
        // TODO: test validations
    }

    /**
     * Returns value of the specified integer64 variable
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readInt64VarTest() throws ApiException {
        String int64Name = null;
        Int64ValueObject response = api.readInt64Var(int64Name);
        // TODO: test validations
    }

    /**
     * Returns value of the specified integer64 variable as a string
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readInt64VarAsStringTest() throws ApiException {
        String int64Name = null;
        Int64StringValueObject response = api.readInt64VarAsString(int64Name);
        // TODO: test validations
    }

    /**
     * Returns the name and value of all integer64 variables in the strategy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readInt64VarsTest() throws ApiException {
        List<Int64Var> response = api.readInt64Vars();
        // TODO: test validations
    }

    /**
     * Returns the name and value as a string of all integer64 variables in the strategy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readInt64VarsAsStringsTest() throws ApiException {
        List<Int64VarAsString> response = api.readInt64VarsAsStrings();
        // TODO: test validations
    }

    /**
     * Returns the name, date, time, and CRC of the strategy currently in the controller, and the number of charts currently running. Empty strings and a 0 will be returned when there is no strategy.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readStrategyDetailsTest() throws ApiException {
        StrategyResponse response = api.readStrategyDetails();
        // TODO: test validations
    }

    /**
     * \&quot;Read a range of table elements from the specified string table\&quot;  #### Examples ####  * Read all elements in a table named strTable: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable  * Read elements 5 and up in a table named i64table starting with index 5: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable?startIndex&#x3D;5  * Read 3 consecutive elements in a table named i64table starting with the element at index 10: https://1.2.3.4/api/v1/device/strategy/tables/strings/strTable?startIndex&#x3D;10&amp;numElements&#x3D;3 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readStringTableTest() throws ApiException {
        String tableName = null;
        Integer startIndex = null;
        Integer numElements = null;
        List<String> response = api.readStringTable(tableName, startIndex, numElements);
        // TODO: test validations
    }

    /**
     * Read specified table element
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readStringTableElementTest() throws ApiException {
        String tableName = null;
        Integer index = null;
        StringValueObject response = api.readStringTableElement(tableName, index);
        // TODO: test validations
    }

    /**
     * Returns an array of the name and length of all the string tables in the strategy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readStringTablesTest() throws ApiException {
        List<TableDef> response = api.readStringTables();
        // TODO: test validations
    }

    /**
     * Returns value of the specified string
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readStringVarTest() throws ApiException {
        String stringName = null;
        StringValueObject response = api.readStringVar(stringName);
        // TODO: test validations
    }

    /**
     * Returns the name and value of all string variables in the strategy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readStringVarsTest() throws ApiException {
        List<StringVar> response = api.readStringVars();
        // TODO: test validations
    }

    /**
     * Returns current value of the specified up timer
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readUpTimerValueTest() throws ApiException {
        String upTimerName = null;
        FloatValueObject response = api.readUpTimerValue(upTimerName);
        // TODO: test validations
    }

    /**
     * Returns the name and current value of all up timers in the strategy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readUpTimerVarsTest() throws ApiException {
        List<FloatVar> response = api.readUpTimerVars();
        // TODO: test validations
    }

    /**
     * Sets the value of the specified analog output point
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeAnalogOutputEuTest() throws ApiException {
        String ioName = null;
        FloatValueObject body = null;
        api.writeAnalogOutputEu(ioName, body);
        // TODO: test validations
    }

    /**
     * Sets the value of the specified digital output point
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeDigitalOutputStateTest() throws ApiException {
        String ioName = null;
        DigitalPointStateObject body = null;
        api.writeDigitalOutputState(ioName, body);
        // TODO: test validations
    }

    /**
     * Write table elements #### Examples #### * Write the values (1.5, 2.4, 3.5) to 3 consecutive elements in a table named ftable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/floats/ftable?startIndex&#x3D;10  with body of the POST request set to [ 1.5, 2.4, 3.5 ] 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeFloatTableTest() throws ApiException {
        String tableName = null;
        List<Float> floatArray = null;
        Integer startIndex = null;
        api.writeFloatTable(tableName, floatArray, startIndex);
        // TODO: test validations
    }

    /**
     * Write specified table element
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeFloatTableElementTest() throws ApiException {
        String tableName = null;
        Integer index = null;
        FloatValueObject floatElementObject = null;
        api.writeFloatTableElement(tableName, index, floatElementObject);
        // TODO: test validations
    }

    /**
     * Sets the value of a float variable
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeFloatVarTest() throws ApiException {
        String floatName = null;
        FloatValueObject body = null;
        api.writeFloatVar(floatName, body);
        // TODO: test validations
    }

    /**
     * \&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named itable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int32s/itable?startIndex&#x3D;10  with body of the POST request set to [ 1, 2, 3 ]       
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeInt32TableTest() throws ApiException {
        String tableName = null;
        List<Integer> int32Array = null;
        Integer startIndex = null;
        api.writeInt32Table(tableName, int32Array, startIndex);
        // TODO: test validations
    }

    /**
     * Write specified integer32 table element
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeInt32TableElementTest() throws ApiException {
        String tableName = null;
        Integer index = null;
        Int32ValueObject int32ElementObject = null;
        api.writeInt32TableElement(tableName, index, int32ElementObject);
        // TODO: test validations
    }

    /**
     * Sets the value of an integer32 variable
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeInt32VarTest() throws ApiException {
        String int32Name = null;
        Int32ValueObject body = null;
        api.writeInt32Var(int32Name, body);
        // TODO: test validations
    }

    /**
     * \&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named i64table starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table?startIndex&#x3D;10  with body of the POST request set to [ 1, 2, 3 ] 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeInt64TableTest() throws ApiException {
        String tableName = null;
        List<Long> int64Array = null;
        Integer startIndex = null;
        api.writeInt64Table(tableName, int64Array, startIndex);
        // TODO: test validations
    }

    /**
     * \&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (1, 2, 3) to 3 consecutive elements in a table named i64table starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/int64s/i64table/_string?startIndex&#x3D;10  with body of the POST request set to [ \&quot;1\&quot;, \&quot;2\&quot;, \&quot;3\&quot; ] 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeInt64TableAsStringTest() throws ApiException {
        String tableName = null;
        List<String> int64AsStringArray = null;
        Integer startIndex = null;
        api.writeInt64TableAsString(tableName, int64AsStringArray, startIndex);
        // TODO: test validations
    }

    /**
     * Write specified integer64 table element
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeInt64TableElementTest() throws ApiException {
        String tableName = null;
        Integer index = null;
        Int64ValueObject int64ElementObject = null;
        api.writeInt64TableElement(tableName, index, int64ElementObject);
        // TODO: test validations
    }

    /**
     * Write specified integer64 table element as string
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeInt64TableElementAsStringTest() throws ApiException {
        String tableName = null;
        Integer index = null;
        Int64StringValueObject int64ElementObject = null;
        api.writeInt64TableElementAsString(tableName, index, int64ElementObject);
        // TODO: test validations
    }

    /**
     * Sets the value of an integer64 variable
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeInt64VarTest() throws ApiException {
        String int64Name = null;
        Int64ValueObject body = null;
        api.writeInt64Var(int64Name, body);
        // TODO: test validations
    }

    /**
     * Sets the value of an integer64 variable as a string
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeInt64VarAsStringTest() throws ApiException {
        String int64Name = null;
        Int64StringValueObject body = null;
        api.writeInt64VarAsString(int64Name, body);
        // TODO: test validations
    }

    /**
     * \&quot;Write a range of table elements\&quot; #### Examples #### * Write the values (\&quot;first\&quot;, \&quot;second\&quot;, \&quot;third\&quot;) to 3 consecutive elements in a table named strTable starting with the element at index 10:POST to https://1.2.3.4/api/v1/device/strategy/tables/strings/strtable?startIndex&#x3D;10  with body of the POST request set to [ \&quot;first\&quot;, \&quot;second\&quot;, \&quot;third\&quot; ] 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeStringTableTest() throws ApiException {
        String tableName = null;
        List<String> stringArray = null;
        Integer startIndex = null;
        ErrorResponse200OKish response = api.writeStringTable(tableName, stringArray, startIndex);
        // TODO: test validations
    }

    /**
     * Write specified table element
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeStringTableElementTest() throws ApiException {
        String tableName = null;
        Integer index = null;
        StringValueObject stringElementObject = null;
        api.writeStringTableElement(tableName, index, stringElementObject);
        // TODO: test validations
    }

    /**
     * Sets the value of a string variable
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeStringVarTest() throws ApiException {
        String stringName = null;
        StringValueObject body = null;
        ErrorResponse200OKish response = api.writeStringVar(stringName, body);
        // TODO: test validations
    }

}
