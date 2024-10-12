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
import org.openapitools.client.model.PatientAuthConfirmRequest;
import org.openapitools.client.model.PatientAuthConfirmResponse;
import org.openapitools.client.model.PatientAuthInitRequest;
import org.openapitools.client.model.PatientAuthInitResponse;
import org.openapitools.client.model.PatientAuthModeQueryRequest;
import org.openapitools.client.model.PatientAuthModeQueryResponse;
import org.openapitools.client.model.PatientAuthNotification;
import org.openapitools.client.model.PatientAuthNotificationAcknowledgement;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for UserAuthApi
 */
@Disabled
public class UserAuthApiTest {

    private final UserAuthApi api = new UserAuthApi();

    /**
     * Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation
     *
     * This API is called by HIP/HIUs to confirm authentication of users. The transactionId returned by the previous callback API /users/auth/on-init must be sent. If Authentication is successful the callback API will send an \&quot;access token\&quot; for subsequent purpose specific API calls. Note only **credential.authCode** or **credential.demographic** should be sent   1. demographic details are only required for  demographic auth as of now.    2. demographic details are required only in MEDIATED cases and if the **auth.mode** so demands. e.g. if **auth.mode** is DEMOGRAPHICS. Usually for demographic authentication, the name, gender and DOB must be exactly as specified in User Account.   3. demographic.identifier is optional, however maybe required if authentication so mandates.    4. credential.authCode is required for other MEDIATED authentication like MOBILE_OTP, AADHAAR_OTP.  
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05UsersAuthConfirmPostTest() throws ApiException {
        String authorization = null;
        String X_CM_ID = null;
        PatientAuthConfirmRequest patientAuthConfirmRequest = null;
        api.v05UsersAuthConfirmPost(authorization, X_CM_ID, patientAuthConfirmRequest);
        // TODO: test validations
    }

    /**
     * Get a patient&#39;s authentication modes relevant to specified purpose
     *
     * This API is meant for identify supported authentication modes for a patient given a specific purpose 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05UsersAuthFetchModesPostTest() throws ApiException {
        String authorization = null;
        String X_CM_ID = null;
        PatientAuthModeQueryRequest patientAuthModeQueryRequest = null;
        api.v05UsersAuthFetchModesPost(authorization, X_CM_ID, patientAuthModeQueryRequest);
        // TODO: test validations
    }

    /**
     * Initialize authentication from HIP
     *
     * This API is called by HIPs to initiate authentication of users. A transactionId is retuned by the corresponding callback API for confirmation of user auth. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05UsersAuthInitPostTest() throws ApiException {
        String authorization = null;
        String X_CM_ID = null;
        PatientAuthInitRequest patientAuthInitRequest = null;
        api.v05UsersAuthInitPost(authorization, X_CM_ID, patientAuthInitRequest);
        // TODO: test validations
    }

    /**
     * notification API in case of DIRECT mode of authentication by the CM
     *
     * This API is called by CM to confirm authentication of users. The transactionId returned is same as that passed in /auth/on-init. The \&quot;auth.status\&quot; conveys whether the request was GRANTED or DENIED.    1. **auth.accessToken** - is specific to the purpose mentioned in the /auth/init. This token needs to be used for initiating the intended action. For example for HIP initiated linking of care-contexts   2. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.   3. The payload is conditional to the purpose of auth. If purpose specified in /auth/init is KYC or KYC_AND_LINK, then patient details are passed. **auth.accessToken** is passed only if the purpose is LINK or KYC_AND_LINK. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05UsersAuthNotifyPostTest() throws ApiException {
        String authorization = null;
        String X_HIP_ID = null;
        String X_HIU_ID = null;
        PatientAuthNotification patientAuthNotification = null;
        api.v05UsersAuthNotifyPost(authorization, X_HIP_ID, X_HIU_ID, patientAuthNotification);
        // TODO: test validations
    }

    /**
     * callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not
     *
     * This API is called by CM to confirm authentication of users.    1. **auth.accessToken** - is specific to the purpose mentioned in the /auth/init. This token needs to be used for initiating the intended action. For example for HIP initiated linking of care-contexts   2. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.      
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05UsersAuthOnConfirmPostTest() throws ApiException {
        String authorization = null;
        String X_HIP_ID = null;
        String X_HIU_ID = null;
        PatientAuthConfirmResponse patientAuthConfirmResponse = null;
        api.v05UsersAuthOnConfirmPost(authorization, X_HIP_ID, X_HIU_ID, patientAuthConfirmResponse);
        // TODO: test validations
    }

    /**
     * Identification result for a consent-manager user-id
     *
     * If a patient is found then **auth** attribute contains the supported modes for the specified purpose.  Otherwise, error is raised for invalid requests or for non-existent id. Note in addition to the \&quot;Authorization\&quot; header, one of the following headers must be specified 1. **X-HIU-ID** if the requester is HIU (identified from /auth/fetch-modes requester.id) 2. **X-HIP-ID** if the requester is HIP (identified from /auth/fetch-modes requester.id) 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05UsersAuthOnFetchModesPostTest() throws ApiException {
        String authorization = null;
        String X_HIP_ID = null;
        String X_HIU_ID = null;
        PatientAuthModeQueryResponse patientAuthModeQueryResponse = null;
        api.v05UsersAuthOnFetchModesPost(authorization, X_HIP_ID, X_HIU_ID, patientAuthModeQueryResponse);
        // TODO: test validations
    }

    /**
     * Response to user authentication initialization from HIP
     *
     * If the patient&#39;s id is valid, CM will return a transactionId as initialization of user auth. If the request is valid, then &#39;auth.mode&#39; will convey how the authentication should be done. The authentication can be *mediated* or *direct*. For mediated authentication modes, HIP or HIU is epected to send over relevant code (OTP/token) or demographic info via subsequent API call to /auth/confirm. for direct authentication case, CM will notify requester through/users/auth/notify API.     1. **auth.mode** conveys whats the mode of authentication is, and what is expected from HIP/HIU in the subsequent /auth/confirm API call. Possible values        1. MOBILE_OTP - auth via OTP to registered mobile. Mediated.        2. AADHAAR_OTP - auth initiated with Aadhaar with OTP. Mediated.        3. DEMOGRAPHICS - auth initiated with demographic verification       4. DIRECT - for authentication directly with the patient. e.g. Mobile App, SMS. In this case, the HIP/HIU is not expected to call subsequent /auth/confirm call. CM will do direct authentication with the User (e.g. Mobile App, SMS etc) and will notify requester   2. **meta.expiry** conveys the expiry time of the token and the authentication session   3. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.                         The error section in the body, represents the potential errors that may have occurred. Possible reasons:   1. Patient id is invalid 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05UsersAuthOnInitPostTest() throws ApiException {
        String authorization = null;
        String X_HIP_ID = null;
        String X_HIU_ID = null;
        PatientAuthInitResponse patientAuthInitResponse = null;
        api.v05UsersAuthOnInitPost(authorization, X_HIP_ID, X_HIU_ID, patientAuthInitResponse);
        // TODO: test validations
    }

    /**
     * callback API by HIU/HIPs as acknowledgement of auth notification
     *
     * This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication.  
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05UsersAuthOnNotifyPostTest() throws ApiException {
        String authorization = null;
        String X_CM_ID = null;
        PatientAuthNotificationAcknowledgement patientAuthNotificationAcknowledgement = null;
        api.v05UsersAuthOnNotifyPost(authorization, X_CM_ID, patientAuthNotificationAcknowledgement);
        // TODO: test validations
    }

}
