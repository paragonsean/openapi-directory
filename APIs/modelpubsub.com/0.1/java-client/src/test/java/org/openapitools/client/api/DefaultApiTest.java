/*
 * defaultTitle
 * defaultDescription
 *
 * The version of the OpenAPI document: 0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Apiv10SafeUnsafeImageWithTagsBody;
import org.openapitools.client.model.InlineResponse200;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * Auto generated using Swagger Inspector
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV10SafeUnsafeImageWithTagsPostTest() throws ApiException {
        Apiv10SafeUnsafeImageWithTagsBody apiv10SafeUnsafeImageWithTagsBody = null;
        InlineResponse200 response = api.apiV10SafeUnsafeImageWithTagsPost(apiv10SafeUnsafeImageWithTagsBody);
        // TODO: test validations
    }

}
