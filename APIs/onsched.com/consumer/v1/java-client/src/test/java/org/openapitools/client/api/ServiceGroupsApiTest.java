/*
 * OnSched Consumer API
 * Build secure and scalable custom apps for Online Booking. Our flexible API provides many options for availability and booking.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ServiceGroupListViewModel;
import org.openapitools.client.model.ServiceGroupViewModel;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ServiceGroupsApi
 */
@Disabled
public class ServiceGroupsApiTest {

    private final ServiceGroupsApi api = new ServiceGroupsApi();

    /**
     * List Service Groups
     *
     * &lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Service Groups&lt;/b&gt; for the requested location. If not specified, the business location defaults to the primary business location. Use the offset and limit parameters to control the page start and size. Default offset is 0, limit is 20, maximum is 100. Use the other query parameters to filter the results further.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void consumerV1ServicegroupsGetTest() throws ApiException {
        String locationId = null;
        Integer offset = null;
        Integer limit = null;
        ServiceGroupListViewModel response = api.consumerV1ServicegroupsGet(locationId, offset, limit);
        // TODO: test validations
    }

    /**
     * Get Service Group
     *
     * &lt;p&gt;Use this endpoint to return a &lt;b&gt;Service Group&lt;/b&gt; object. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. Find serviceGroup id&#39;s by using the &lt;i&gt;GET /consumer/v1/serviceGroups&lt;/i&gt; endpoint.&lt;/p&gt;
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void consumerV1ServicegroupsIdGetTest() throws ApiException {
        Integer id = null;
        ServiceGroupViewModel response = api.consumerV1ServicegroupsIdGet(id);
        // TODO: test validations
    }

}
