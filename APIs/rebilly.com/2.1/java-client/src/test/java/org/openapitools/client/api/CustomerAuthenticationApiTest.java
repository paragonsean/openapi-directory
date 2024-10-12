/*
 * Rebilly REST API
 * # Introduction The Rebilly API is built on HTTP.  Our API is RESTful.  It has predictable resource URLs.  It returns HTTP response codes to indicate errors.  It also accepts and returns JSON in the HTTP body.  You can use your favorite HTTP/REST library for your programming language to use Rebilly's API, or you can use one of our SDKs (currently available in [PHP](https://github.com/Rebilly/rebilly-php) and [Javascript](https://github.com/Rebilly/rebilly-js-sdk)).  We have other APIs that are also available.  Every action from our [app](https://app.rebilly.com) is supported by an API which is documented and available for use so that you may automate any workflows necessary.  This document contains the most commonly integrated resources.  # Authentication  When you sign up for an account, you are given your first secret API key. You can generate additional API keys, and delete API keys (as you may need to rotate your keys in the future). You authenticate to the Rebilly API by providing your secret key in the request header.  Rebilly offers three forms of authentication:  secret key, publishable key, JSON Web Tokens, and public signature key. - [Secret API key](#section/Authentication/SecretApiKey): used for requests made   from the server side. Never share these keys. Keep them guarded and secure. - [Publishable API key](#section/Authentication/PublishableApiKey): used for    requests from the client side. For now can only be used to create    a [Payment Token](#operation/PostToken) and    a [File token](#operation/PostFile). - [JWT](#section/Authentication/JWT): short lifetime tokens that can be assigned a specific expiration time.  Never share your secret keys. Keep them guarded and secure.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # Errors Rebilly follow's the error response format proposed in [RFC 7807](https://tools.ietf.org/html/rfc7807) also known as Problem Details for HTTP APIs.  As with our normal API responses, your client must be prepared to gracefully handle additional members of the response.  ## Forbidden &lt;RedocResponse pointer={\"#/components/responses/Forbidden\"} /&gt;  ## Conflict &lt;RedocResponse pointer={\"#/components/responses/Conflict\"} /&gt;  ## NotFound &lt;RedocResponse pointer={\"#/components/responses/NotFound\"} /&gt;  ## Unauthorized &lt;RedocResponse pointer={\"#/components/responses/Unauthorized\"} /&gt;  ## ValidationError &lt;RedocResponse pointer={\"#/components/responses/ValidationError\"} /&gt;  # SDKs  Rebilly offers a Javascript SDK and a PHP SDK to help interact with the API.  However, no SDK is required to use the API.  Rebilly also offers [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/),  a client-side iFrame-based solution to help create payment tokens while minimizing PCI DSS compliance burdens and maximizing the customizability. [FramePay](https://docs.rebilly.com/docs/developer-docs/framepay/) is interacting with the [payment tokens creation operation](#operation/PostToken).  ## Javascript SDK  Installation and usage instructions can be found [here](https://docs.rebilly.com/docs/developer-docs/sdks). SDK code examples are included in these docs.  ## PHP SDK For all PHP SDK examples provided in these docs you will need to configure the `$client`. You may do it like this:  ```php $client = new Rebilly\\Client([     'apiKey' =&gt; 'YourApiKeyHere',     'baseUrl' =&gt; 'https://api.rebilly.com', ]); ```  # Using filter with collections Rebilly provides collections filtering. You can use `?filter` param on collections to define which records should be shown in the response.  Here is filter format description:  - Fields and values in filter are separated with `:`: `?filter=firstName:John`.  - Sub-fields are separated with `.`: `?filter=billingAddress.country:US`.  - Multiple filters are separated with `;`: `?filter=firstName:John;lastName:Doe`. They will be joined with `AND` logic. In this example: `firstName:John` AND `lastName:Doe`.  - You can use multiple values using `,` as values separator: `?filter=firstName:John,Bob`. Multiple values specified for a field will be joined with `OR` logic. In this example: `firstName:John` OR `firstName:Bob`.  - To negate the filter use `!`: `?filter=firstName:!John`. Note that you can negate multiple values like this: `?filter=firstName:!John,!Bob`. This filter rule will exclude all Johns and Bobs from the response.  - You can use range filters like this: `?filter=amount:1..10`.  - You can use gte (greater than or equals) filter like this: `?filter=amount:1..`, or lte (less than or equals) than filter like this: `?filter=amount:..10`. This also works for datetime-based fields.  - You can create some [predefined values lists](https://user-api-docs.rebilly.com/#tag/Lists) and use them in filter: `?filter=firstName:@yourListName`. You can also exclude list values: `?filter=firstName:!@yourListName`.  - Datetime-based fields accept values formatted using RFC 3339 like this: `?filter=createdTime:2021-02-14T13:30:00Z`.   # Expand to include embedded objects Rebilly provides the ability to pre-load additional  objects with a request.   You can use `?expand` param on most requests to expand and include embedded objects within the `_embedded` property of the response.  The `_embedded` property contains an array of  objects keyed by the expand parameter value(s).  You may expand multiple objects by passing them as comma-separated to the expand value like so:  ``` ?expand=recentInvoice,customer ```  And in the response, you would see:  ``` \"_embedded\": [     \"recentInvoice\": {...},     \"customer\": {...} ] ``` Expand may be utilitized not only on `GET` requests but also on `PATCH`, `POST`, `PUT` requests too.   # Getting started guide  Rebilly's API has over 300 operations.  That's more than you'll  need to implement your use cases.  If you have a use  case you would like to implement, please consult us for feedback on the best API operations for the task.  Our getting started guide will demonstrate a basic order form use case.  It will allow us to highlight core resources in Rebilly that will be helpful for many other use cases too.  Within 25 minutes, you'll have sent API requests (via our console) to create a subscription order. 
 *
 * The version of the OpenAPI document: 2.1
 * Contact: integrations@rebilly.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.AuthenticationOptions;
import org.openapitools.client.model.AuthenticationToken;
import org.openapitools.client.model.Credential;
import org.openapitools.client.model.CustomerJWT;
import org.openapitools.client.model.Error;
import org.openapitools.client.model.InvalidError;
import org.openapitools.client.model.ResetPasswordToken;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for CustomerAuthenticationApi
 */
@Disabled
public class CustomerAuthenticationApiTest {

    private final CustomerAuthenticationApi api = new CustomerAuthenticationApi();

    /**
     * Logout a customer
     *
     * Logout a customer. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteAuthenticationTokenTest() throws ApiException {
        String token = null;
        String organizationId = null;
        api.deleteAuthenticationToken(token, organizationId);
        // TODO: test validations
    }

    /**
     * Delete a credential
     *
     * Delete a credential with predefined identifier string. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteCredentialTest() throws ApiException {
        String id = null;
        String organizationId = null;
        api.deleteCredential(id, organizationId);
        // TODO: test validations
    }

    /**
     * Delete a Reset Password Token
     *
     * Delete a Reset Password Token with predefined identifier string. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deletePasswordTokenTest() throws ApiException {
        String id = null;
        String organizationId = null;
        api.deletePasswordToken(id, organizationId);
        // TODO: test validations
    }

    /**
     * Read current authentication options
     *
     * Read current authentication options. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAuthenticationOptionTest() throws ApiException {
        String organizationId = null;
        List<AuthenticationOptions> response = api.getAuthenticationOption(organizationId);
        // TODO: test validations
    }

    /**
     * Retrieve a list of auth tokens
     *
     * Retrieve a list of auth tokens. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAuthenticationTokenCollectionTest() throws ApiException {
        String organizationId = null;
        Integer limit = null;
        Integer offset = null;
        List<AuthenticationToken> response = api.getAuthenticationTokenCollection(organizationId, limit, offset);
        // TODO: test validations
    }

    /**
     * Verify
     *
     * Verify an authentication token. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAuthenticationTokenVerificationTest() throws ApiException {
        String token = null;
        String organizationId = null;
        AuthenticationToken response = api.getAuthenticationTokenVerification(token, organizationId);
        // TODO: test validations
    }

    /**
     * Retrieve a credential
     *
     * Retrieve a credential with specified identifier string. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCredentialTest() throws ApiException {
        String id = null;
        String organizationId = null;
        Credential response = api.getCredential(id, organizationId);
        // TODO: test validations
    }

    /**
     * Retrieve a list of credentials
     *
     * Retrieve a list of credentials. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getCredentialCollectionTest() throws ApiException {
        String organizationId = null;
        Integer limit = null;
        Integer offset = null;
        List<Credential> response = api.getCredentialCollection(organizationId, limit, offset);
        // TODO: test validations
    }

    /**
     * Retrieve a Reset Password Token
     *
     * Retrieve a Reset Password Token with specified identifier string. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPasswordTokenTest() throws ApiException {
        String id = null;
        String organizationId = null;
        ResetPasswordToken response = api.getPasswordToken(id, organizationId);
        // TODO: test validations
    }

    /**
     * Retrieve a list of tokens
     *
     * Retrieve a list of tokens. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPasswordTokenCollectionTest() throws ApiException {
        String organizationId = null;
        Integer limit = null;
        Integer offset = null;
        List<ResetPasswordToken> response = api.getPasswordTokenCollection(organizationId, limit, offset);
        // TODO: test validations
    }

    /**
     * Login
     *
     * Login a customer. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postAuthenticationTokenTest() throws ApiException {
        AuthenticationToken authenticationToken = null;
        String organizationId = null;
        AuthenticationToken response = api.postAuthenticationToken(authenticationToken, organizationId);
        // TODO: test validations
    }

    /**
     * Exchange
     *
     * Exchange Authentication Token for JWT.  It will also invalidate an Authentication Token by default (so it can only be exchanged once). 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postAuthenticationTokenExchangeTest() throws ApiException {
        String token = null;
        CustomerJWT customerJWT = null;
        String organizationId = null;
        CustomerJWT response = api.postAuthenticationTokenExchange(token, customerJWT, organizationId);
        // TODO: test validations
    }

    /**
     * Create a credential
     *
     * Create a credential. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postCredentialTest() throws ApiException {
        Credential credential = null;
        String organizationId = null;
        Credential response = api.postCredential(credential, organizationId);
        // TODO: test validations
    }

    /**
     * Create a Reset Password Token
     *
     * Create a Reset Password Token. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void postPasswordTokenTest() throws ApiException {
        ResetPasswordToken resetPasswordToken = null;
        String organizationId = null;
        ResetPasswordToken response = api.postPasswordToken(resetPasswordToken, organizationId);
        // TODO: test validations
    }

    /**
     * Change authentication options
     *
     * Change options. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putAuthenticationOptionTest() throws ApiException {
        AuthenticationOptions authenticationOptions = null;
        String organizationId = null;
        AuthenticationOptions response = api.putAuthenticationOption(authenticationOptions, organizationId);
        // TODO: test validations
    }

    /**
     * Create or update a credential with predefined ID
     *
     * Create or update a credential with predefined identifier string. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void putCredentialTest() throws ApiException {
        String id = null;
        Credential credential = null;
        String organizationId = null;
        Credential response = api.putCredential(id, credential, organizationId);
        // TODO: test validations
    }

}
