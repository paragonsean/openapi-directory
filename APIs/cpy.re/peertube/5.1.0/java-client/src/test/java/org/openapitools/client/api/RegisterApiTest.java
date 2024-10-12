/*
 * PeerTube
 * The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api/rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api/rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/_*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/_*`                    | | `/download/_*`               | | `/lazy-static/_*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins. 
 *
 * The version of the OpenAPI document: 5.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ListRegistrations200Response;
import org.openapitools.client.model.RegisterUser;
import org.openapitools.client.model.ResendEmailToVerifyRegistrationRequest;
import org.openapitools.client.model.ResendEmailToVerifyUserRequest;
import org.openapitools.client.model.UserRegistration;
import org.openapitools.client.model.UserRegistrationAcceptOrReject;
import org.openapitools.client.model.UserRegistrationRequest;
import org.openapitools.client.model.VerifyRegistrationEmailRequest;
import org.openapitools.client.model.VerifyUserRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for RegisterApi
 */
@Disabled
public class RegisterApiTest {

    private final RegisterApi api = new RegisterApi();

    /**
     * Accept registration
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void acceptRegistrationTest() throws ApiException {
        Integer registrationId = null;
        UserRegistrationAcceptOrReject userRegistrationAcceptOrReject = null;
        api.acceptRegistration(registrationId, userRegistrationAcceptOrReject);
        // TODO: test validations
    }

    /**
     * Delete registration
     *
     * Delete the registration entry. It will not remove the user associated with this registration (if any)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteRegistrationTest() throws ApiException {
        Integer registrationId = null;
        api.deleteRegistration(registrationId);
        // TODO: test validations
    }

    /**
     * List registrations
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listRegistrationsTest() throws ApiException {
        Integer start = null;
        Integer count = null;
        String search = null;
        String sort = null;
        ListRegistrations200Response response = api.listRegistrations(start, count, search, sort);
        // TODO: test validations
    }

    /**
     * Register a user
     *
     * Signup has to be enabled and signup approval is not required
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void registerUserTest() throws ApiException {
        RegisterUser registerUser = null;
        api.registerUser(registerUser);
        // TODO: test validations
    }

    /**
     * Reject registration
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void rejectRegistrationTest() throws ApiException {
        Integer registrationId = null;
        UserRegistrationAcceptOrReject userRegistrationAcceptOrReject = null;
        api.rejectRegistration(registrationId, userRegistrationAcceptOrReject);
        // TODO: test validations
    }

    /**
     * Request registration
     *
     * Signup has to be enabled and require approval on the instance
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void requestRegistrationTest() throws ApiException {
        UserRegistrationRequest userRegistrationRequest = null;
        UserRegistration response = api.requestRegistration(userRegistrationRequest);
        // TODO: test validations
    }

    /**
     * Resend verification link to registration email
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resendEmailToVerifyRegistrationTest() throws ApiException {
        ResendEmailToVerifyRegistrationRequest resendEmailToVerifyRegistrationRequest = null;
        api.resendEmailToVerifyRegistration(resendEmailToVerifyRegistrationRequest);
        // TODO: test validations
    }

    /**
     * Resend user verification link
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resendEmailToVerifyUser_0Test() throws ApiException {
        ResendEmailToVerifyUserRequest resendEmailToVerifyUserRequest = null;
        api.resendEmailToVerifyUser_0(resendEmailToVerifyUserRequest);
        // TODO: test validations
    }

    /**
     * Verify a registration email
     *
     * Following a user registration request, the user will receive an email asking to click a link containing a secret. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void verifyRegistrationEmailTest() throws ApiException {
        Integer registrationId = null;
        VerifyRegistrationEmailRequest verifyRegistrationEmailRequest = null;
        api.verifyRegistrationEmail(registrationId, verifyRegistrationEmailRequest);
        // TODO: test validations
    }

    /**
     * Verify a user
     *
     * Following a user registration, the new user will receive an email asking to click a link containing a secret. This endpoint can also be used to verify a new email set in the user account. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void verifyUser_0Test() throws ApiException {
        Integer id = null;
        VerifyUserRequest verifyUserRequest = null;
        api.verifyUser_0(id, verifyUserRequest);
        // TODO: test validations
    }

}
