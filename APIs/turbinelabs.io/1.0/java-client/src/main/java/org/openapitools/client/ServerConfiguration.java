/*
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client;

import java.util.Map;

/**
 * Representing a Server configuration.
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T09:56:51.953320-04:00[America/New_York]", comments = "Generator version: 7.9.0")
public class ServerConfiguration {
    public String URL;
    public String description;
    public Map<String, ServerVariable> variables;

    /**
     * @param URL A URL to the target host.
     * @param description A description of the host designated by the URL.
     * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
     */
    public ServerConfiguration(String URL, String description, Map<String, ServerVariable> variables) {
        this.URL = URL;
        this.description = description;
        this.variables = variables;
    }

    /**
     * Format URL template using given variables.
     *
     * @param variables A map between a variable name and its value.
     * @return Formatted URL.
     */
    public String URL(Map<String, String> variables) {
        String url = this.URL;

        // go through variables and replace placeholders
        for (Map.Entry<String, ServerVariable> variable: this.variables.entrySet()) {
            String name = variable.getKey();
            ServerVariable serverVariable = variable.getValue();
            String value = serverVariable.defaultValue;

            if (variables != null && variables.containsKey(name)) {
                value = variables.get(name);
                if (serverVariable.enumValues.size() > 0 && !serverVariable.enumValues.contains(value)) {
                    throw new IllegalArgumentException("The variable " + name + " in the server URL has invalid value " + value + ".");
                }
            }
            url = url.replace("{" + name + "}", value);
        }
        return url;
    }

    /**
     * Format URL template using default server variables.
     *
     * @return Formatted URL.
     */
    public String URL() {
        return URL(null);
    }
}
