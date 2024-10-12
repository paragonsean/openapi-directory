/*
 * TruAnon Private API
 * Welcome to TruAnon! Thank you for helping make the Internet a safer place to be.  Adopting TruAnon is simple. There is no setup or dependencies, nothing to store or process. Making identity part of your service is fun, and you’ll be up and running in a matter of minutes.  TruAnon Private Token is used anytime you request information from TruAnon and you must edit this into the Variables section for this collection.  This API contains two endpoints and both require these same two arguments, also found in the Variables section of this collection.  These two arguments are:  TruAnon Service Identifier  and  Your Member Name  Your TruAnon Service Identifier was provided by TruAnon and is likely the root domain of your site or service. Your Member Name is the unique member ID on your system that you would like to query.  Information is continuously updated for display purposes and aside from performance considerations, there should be no need to capture or save anything from TruAnon.
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
 * API tests for DefaultApi
 */
@Disabled
public class DefaultApiTest {

    private final DefaultApi api = new DefaultApi();

    /**
     * Get Profile
     *
     * get_profile Private API: Request confirmed profile data for your unique member ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getProfileTest() throws ApiException {
        String id = null;
        String service = null;
        api.getProfile(id, service);
        // TODO: test validations
    }

    /**
     * Get Token
     *
     * request_token Private API: Request a Proof token to let the member confirm in a popup interface          {\&quot;id\&quot;:\&quot;qjgblv72bzzio\&quot;,\&quot;type\&quot;:\&quot;Proof\&quot;,\&quot;active\&quot;:true,\&quot;name\&quot;:\&quot;New Proof\&quot;}  Step 2. Create a verifyProfile Public Web link: Use the Proof token id as the token argument in your public URL used to open a new target popup. This activity is where members may confirm immediately.              https://staging.truanon.com/verifyProfile?id&#x3D;john_doe&amp;service&#x3D;securecannabisalliance&amp;token&#x3D;qjgblv72bzzio
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTokenTest() throws ApiException {
        String id = null;
        String service = null;
        api.getToken(id, service);
        // TODO: test validations
    }

}
