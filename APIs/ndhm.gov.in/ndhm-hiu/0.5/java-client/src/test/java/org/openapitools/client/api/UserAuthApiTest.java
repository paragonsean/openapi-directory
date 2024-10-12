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


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ErrorResponse;
import org.openapitools.client.model.PatientAuthConfirmResponse;
import org.openapitools.client.model.PatientAuthInitResponse;
import org.openapitools.client.model.PatientAuthModeQueryResponse;
import org.openapitools.client.model.PatientAuthNotification;
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
     * If the patient&#39;s id is valid, CM will return a transactionId as initialization of user auth. If the request is valid, then &#39;auth.mode&#39; will convey how the authentication should be done. The authentication can be *mediated* or *direct*. For mediated authentication modes, HIP or HIU is epected to send over relevant code (OTP/token) or demographic info via subsequent API call to /auth/confirm. for direct authentication case, CM will notify requester through/users/auth/notify API.     1. **auth.mode** conveys whats the mode of authentication is, and what is expected from HIP/HIU in the subsequent /auth/confirm API call. Possible values        1. MOBILE_OTP - auth via OTP to registered mobile. Mediated.        2. AADHAAR_OTP - auth initiated with Aadhaar with OTP. Mediated.        3. DEMOGRAPHICS - auth initiated with demographic verification       4. DIRECT - for authentication directly with the patient. e.g. Mobile App, SMS. In this case, the HIP/HIU is not expected to call subsequent /auth/confirm call. CM will do direct authentication with the User (e.g. Mobile App, SMS etc) and will notify requester   2. **meta.expiry** conveys the expiry time of the token and the authentication session   3. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.    4. **NOTE**, only KYC purpose is applicable for HIU                        The error section in the body, represents the potential errors that may have occurred. Possible reasons:   1. Patient id is invalid 
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

}
