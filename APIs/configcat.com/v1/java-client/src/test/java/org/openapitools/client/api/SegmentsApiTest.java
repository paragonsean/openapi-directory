/*
 * ConfigCat Public Management API
 * **Base API URL**: https://api.configcat.com  If you prefer the swagger documentation, you can find it here: [Swagger UI](https://api.configcat.com/swagger).  The purpose of this API is to access the ConfigCat platform programmatically.  You can **Create**, **Read**, **Update** and **Delete** any entities like **Feature Flags, Configs, Environments** or **Products** within ConfigCat.   The API is based on HTTP REST, uses resource-oriented URLs, status codes and supports JSON  and JSON+HAL format. Do not use this API for accessing and evaluating feature flag values. Use the [SDKs instead](https://configcat.com/docs/sdk-reference/overview).   # OpenAPI Specification  The complete specification is publicly available here: [swagger.json](v1/swagger.json).  You can use it to generate client libraries in various languages with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) or [Swagger Codegen](https://swagger.io/tools/swagger-codegen/) to interact with this API.  # Authentication This API uses the [Basic HTTP Authentication Scheme](https://en.wikipedia.org/wiki/Basic_access_authentication).   <!-- ReDoc-Inject: <security-definitions> -->  # Throttling and rate limits All the rate limited API calls are returning information about the current rate limit period in the following HTTP headers:  | Header | Description | | :- | :- | | X-Rate-Limit-Remaining | The maximum number of requests remaining in the current rate limit period. | | X-Rate-Limit-Reset     | The time when the current rate limit period resets.        |  When the rate limit is exceeded by a request, the API returns with a `HTTP 429 - Too many requests` status along with a `Retry-After` HTTP header. 
 *
 * The version of the OpenAPI document: v1
 * Contact: support@configcat.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CreateSegmentModel;
import org.openapitools.client.model.SegmentListModel;
import org.openapitools.client.model.SegmentListModelHaljson;
import org.openapitools.client.model.SegmentModel;
import org.openapitools.client.model.SegmentModelHaljson;
import java.util.UUID;
import org.openapitools.client.model.UpdateSegmentModel;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SegmentsApi
 */
@Disabled
public class SegmentsApiTest {

    private final SegmentsApi api = new SegmentsApi();

    /**
     * Create Segment
     *
     * This endpoint creates a new Segment in a specified Product  identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createSegmentTest() throws ApiException {
        UUID productId = null;
        CreateSegmentModel createSegmentModel = null;
        SegmentModelHaljson response = api.createSegment(productId, createSegmentModel);
        // TODO: test validations
    }

    /**
     * Delete Segment
     *
     * This endpoint removes a Segment identified by the &#x60;segmentId&#x60; parameter.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteSegmentTest() throws ApiException {
        UUID segmentId = null;
        api.deleteSegment(segmentId);
        // TODO: test validations
    }

    /**
     * Get Segment
     *
     * This endpoint returns the metadata of a Segment identified by the &#x60;segmentId&#x60;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getSegmentTest() throws ApiException {
        UUID segmentId = null;
        SegmentModelHaljson response = api.getSegment(segmentId);
        // TODO: test validations
    }

    /**
     * List Segments
     *
     * This endpoint returns the list of the Segments that belongs to the given Product identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getSegmentsTest() throws ApiException {
        UUID productId = null;
        List<SegmentListModelHaljson> response = api.getSegments(productId);
        // TODO: test validations
    }

    /**
     * Update Segment
     *
     * This endpoint updates a Segment identified by the &#x60;segmentId&#x60; parameter.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateSegmentTest() throws ApiException {
        UUID segmentId = null;
        UpdateSegmentModel updateSegmentModel = null;
        SegmentModelHaljson response = api.updateSegment(segmentId, updateSegmentModel);
        // TODO: test validations
    }

}
