/*
 * Health Repository Provider Specifications for HIU
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **_/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **_/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **_/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent  
 *
 * The version of the OpenAPI document: 0.5
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
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2024-10-12T10:11:36.866529-04:00[America/New_York]", comments = "Generator version: 7.9.0")
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
