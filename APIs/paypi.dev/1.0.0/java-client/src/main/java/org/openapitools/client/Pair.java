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


package org.openapitools.client;

@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:19.161642-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class Pair {
    private String name = "";
    private String value = "";

    public Pair (String name, String value) {
        setName(name);
        setValue(value);
    }

    private void setName(String name) {
        if (!isValidString(name)) {
            return;
        }

        this.name = name;
    }

    private void setValue(String value) {
        if (!isValidString(value)) {
            return;
        }

        this.value = value;
    }

    public String getName() {
        return this.name;
    }

    public String getValue() {
        return this.value;
    }

    private boolean isValidString(String arg) {
        if (arg == null) {
            return false;
        }

        return true;
    }
}
