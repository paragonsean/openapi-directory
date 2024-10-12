/*
 * EtMDB REST API v1
 * The Ethiopian Movie Database
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for PeopleApi
 */
@Disabled
public class PeopleApiTest {

    private final PeopleApi api = new PeopleApi();

    /**
     * Return cast search result
     *
     * Return cast search result  ### Response Class (Status 200) __{param}__ argument can be * artist first name * artist last name * artist username  For more details on how cast are listed [see here][ref]. [ref]: https://etmdb.com/en/cast-list/-updated_date
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void peopleSearchReadTest() throws ApiException {
        String user = null;
        api.peopleSearchRead(user);
        // TODO: test validations
    }

}
