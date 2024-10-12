/*
 * EmailVerify
 * OTP email verification API by PayPI. <br/><br/> EmailVerify provides a simple way to verify email addresses. We send emails ourselves taking the burden of setting up email systems and tracking codes. <br/><br/> To learn more about this API, check out [EmailVerify documentation](https://emailverify.paypi.dev/) <br/><br/>  ## Authentication All requests to the EmailVerify API must be authenticated with an API Key. To get an API key, subscribe to the EmailVerify [here](https://app.paypi.dev/subscribe/c2VydmljZTo1OGQxZDNmMy05OWQ5LTQ3ZjYtOWJkNi02OWNkMTY1OGFmOWU=).  \\ Set your `Authorization` header to `Bearer YOUR-API-KEY`.  ``` curl -H \"Content-Type: application/json\" \\ -H \"Authorization: Bearer YOUR-API-KEY\" \\ ... ``` 
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: hello@paypi.dev
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.Arrays;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for CheckCodePostRequest
 */
public class CheckCodePostRequestTest {
    private final CheckCodePostRequest model = new CheckCodePostRequest();

    /**
     * Model tests for CheckCodePostRequest
     */
    @Test
    public void testCheckCodePostRequest() {
        // TODO: test CheckCodePostRequest
    }

    /**
     * Test the property 'code'
     */
    @Test
    public void codeTest() {
        // TODO: test code
    }

    /**
     * Test the property 'email'
     */
    @Test
    public void emailTest() {
        // TODO: test email
    }

}
