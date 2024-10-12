/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ErrorResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CustomerGroupsIdPermissionsApi
 */
@Disabled
public class CustomerGroupsIdPermissionsApiTest {

    private final CustomerGroupsIdPermissionsApi api = new CustomerGroupsIdPermissionsApi();

    /**
     * customerGroups/{id}/permissions
     *
     * Check if customer group can be deleted.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void customerGroupManagementV1IsReadonlyGetTest() throws ApiException {
        Integer id = null;
        Boolean response = api.customerGroupManagementV1IsReadonlyGet(id);
        // TODO: test validations
    }

}
