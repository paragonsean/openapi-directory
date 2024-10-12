/*
 * groov View Public API
 * #### Revised: 2019-11-21  ### Overview groov View Public API revision 1. 
 *
 * The version of the OpenAPI document: R4.2a
 * Contact: developer@opto22.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import java.math.BigDecimal;
import org.openapitools.client.model.DataStoreDevice;
import org.openapitools.client.model.TagDefinition;
import org.openapitools.client.model.TagReference;
import org.openapitools.client.model.TagValue;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DataStoreApi
 */
@Disabled
public class DataStoreApiTest {

    private final DataStoreApi api = new DataStoreApi();

    /**
     * Read selected tags from the data store. Authorized for admins and editors.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void batchReadTagsTest() throws ApiException {
        List<TagReference> tags = null;
        List<TagValue> response = api.batchReadTags(tags);
        // TODO: test validations
    }

    /**
     * List all data store tags defined in the project. Authorized for admins and editors.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listAllTagsTest() throws ApiException {
        List<TagDefinition> response = api.listAllTags();
        // TODO: test validations
    }

    /**
     * List tags of the given device. Authorized for admins and editors.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listDeviceTagsTest() throws ApiException {
        BigDecimal id = null;
        List<TagDefinition> response = api.listDeviceTags(id);
        // TODO: test validations
    }

    /**
     * List devices available in the data store. Authorized for admins and editors.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listDevicesTest() throws ApiException {
        List<DataStoreDevice> response = api.listDevices();
        // TODO: test validations
    }

    /**
     * Read the current value of a single tag. Authorized for admins and editors.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void readTagTest() throws ApiException {
        BigDecimal id = null;
        BigDecimal index = null;
        BigDecimal count = null;
        TagValue response = api.readTag(id, index, count);
        // TODO: test validations
    }

    /**
     * Writes a new value to the given tag. Authorized for admins and editors.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void writeTagTest() throws ApiException {
        BigDecimal id = null;
        String value = null;
        BigDecimal index = null;
        TagValue response = api.writeTag(id, value, index);
        // TODO: test validations
    }

}
