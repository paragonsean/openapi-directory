/*
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ErrorResponse;
import org.openapitools.client.model.HIPHIRequest;
import org.openapitools.client.model.HIPHealthInformationRequestAcknowledgement;
import org.openapitools.client.model.HIRequest;
import org.openapitools.client.model.HIUHealthInformationRequestResponse;
import org.openapitools.client.model.HealthInformationNotification;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DataFlowApi
 */
@Disabled
public class DataFlowApiTest {

    private final DataFlowApi api = new DataFlowApi();

    /**
     * Health information data request
     *
     * Callback API for acknowledgement of Health information request of HIU. CM calls this API when it has validated the Health Information request given the consent id. Either the **hiRequest** or **error** would need to be specified. If the health info request was valid, then the ***hiRequest.transactionId*** specifies the transaction context against which HIP would send over the data.  Possible cases of errors are   1. **Invalid consent artefact id**   2. **Consent has expired**   3. **Date ranges are invalid** 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05HealthInformationCmOnRequestPostTest() throws ApiException {
        String authorization = null;
        String X_HIU_ID = null;
        HIUHealthInformationRequestResponse hiUHealthInformationRequestResponse = null;
        api.v05HealthInformationCmOnRequestPost(authorization, X_HIU_ID, hiUHealthInformationRequestResponse);
        // TODO: test validations
    }

    /**
     * Health information data request
     *
     * Request for Health information against a consent id. CM would generate a transactionId against each consent and pass it as trnasaction context / correlation id to the HIP and also return the same to HIU via /on-request.  
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05HealthInformationCmRequestPostTest() throws ApiException {
        String authorization = null;
        String X_CM_ID = null;
        HIRequest hiRequest = null;
        api.v05HealthInformationCmRequestPost(authorization, X_CM_ID, hiRequest);
        // TODO: test validations
    }

    /**
     * Health information data request
     *
     * API called by HIP to acknowledge Health information request receipt. Either the **hiRequest** or **error** must be specified. **hiRequest** element returns the same transactionId as before with a status indicating that the request is acknowledged.   
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05HealthInformationHipOnRequestPostTest() throws ApiException {
        String authorization = null;
        String X_CM_ID = null;
        HIPHealthInformationRequestAcknowledgement hiPHealthInformationRequestAcknowledgement = null;
        api.v05HealthInformationHipOnRequestPost(authorization, X_CM_ID, hiPHealthInformationRequestAcknowledgement);
        // TODO: test validations
    }

    /**
     * Health information data request
     *
     * API called by CM to request Health information from HIP against a validated consent artefact. The transactionId is the correlation id that HIP should use use when pushing data to the **dataPushUrl**.  
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05HealthInformationHipRequestPostTest() throws ApiException {
        String authorization = null;
        String X_HIP_ID = null;
        HIPHIRequest hiPHIRequest = null;
        api.v05HealthInformationHipRequestPost(authorization, X_HIP_ID, hiPHIRequest);
        // TODO: test validations
    }

    /**
     * Notifications corresponding to events during data flow
     *
     * API called by HIU and HIP during data-transfer.  1. HIP on transfer of data would send **sessionStatus** - one of [TRANSFERRED, FAILED] 2. HIP would also send **hiStatus** for each *careContextReference* - on of [DELIVERED, ERRORED] 3. HIU on receipt of data would send **sessionStatus** - one of [TRANSFERRED, FAILED]. For example, FAILED when if data was not sent or if invalid data was sent 4. HIU would also send **hiStatus** for each *careContextReference* - one of [OK, ERRORED]  
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05HealthInformationNotifyPostTest() throws ApiException {
        String authorization = null;
        String X_CM_ID = null;
        HealthInformationNotification healthInformationNotification = null;
        api.v05HealthInformationNotifyPost(authorization, X_CM_ID, healthInformationNotification);
        // TODO: test validations
    }

}
