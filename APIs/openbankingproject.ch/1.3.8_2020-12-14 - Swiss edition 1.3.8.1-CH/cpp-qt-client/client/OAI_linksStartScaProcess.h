/**
 * Swiss NextGen Banking API-Framework
 * # Summary The **Swiss NextGen API** is based on the NextGenPSD2 *Framework Version 1.3.4* of the Berlin Group which offers a modern, open, harmonised and interoperable set of Application Programming Interfaces (APIs) as the safest and most efficient way to provide data securely. The NextGen Framework reduces XS2A complexity and costs, addresses the problem of multiple competing standards in Europe and, aligned with the goals of the Euro Retail Payments Board, enables European banking customers to benefit from innovative products and services ('Banking as a Service') by granting TPPs safe and secure (authenticated and authorised) access to their bank accounts and financial data.  The Swiss edtion refines the message formats specific to Switzerland and defines some matching examples.  The possible Approaches are:   * Redirect SCA Approach   * *(Not recommended by obp.ch community) OAuth SCA Approach*   * *(Not recommended by obp.ch community) Decoupled SCA Approach*   * *(Not recommended by obp.ch community) Embedded SCA Approach without SCA method*   * *(Not recommended by obp.ch community) Embedded SCA Approach with only one SCA method available*   * *(Not recommended by obp.ch community) Embedded SCA Approach with Selection of a SCA method*    Not every message defined in this API definition is necessary for all approaches.   Furthermore this API definition does not differ between methods which are mandatory, conditional, or optional   Therefore for a particular implementation of a compliant API it is only necessary to support   a certain subset of the methods defined in this API definition.    **Please have a look at the implementation guidelines if you are not sure   which message has to be used for the approach you are going to use.**  ## Some General Remarks Related to this version of the OpenAPI Specification: * **This API definition is based on the Implementation Guidelines of the [Berlin Group API](https://www.berlin-group.org/nextgenpsd2-downloads).**   It is not a replacement in any sense.   The main specification is (at the moment) always the Implementation Guidelines of the Berlin Group API. * **This API definition contains the REST-API for requests from the PISP to the ASPSP.** * **This API definition contains the messages for all different approaches defined in the Implementation Guidelines.** * According to the OpenAPI-Specification [https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md]      \"If in is \"header\" and the name field is \"Accept\", \"Content-Type\" or \"Authorization\", the parameter definition SHALL be ignored.\"    The element \"Accept\" will not be defined in this file at any place.    The elements \"Content-Type\" and \"Authorization\" are implicitly defined by the OpenApi tags \"content\" and \"security\".  * There are several predefined types which might occur in payment initiation messages,   but are not used in the standard JSON messages in the Implementation Guidelines.   Therefore they are not used in the corresponding messages in this file either.   We added them for the convenience of the user.   If there is a payment product, which needs these fields, one can easily use the predefined types.   But the ASPSP need not to accept them in general.  * **We omit the definition of all standard HTTP header elements (mandatory/optional/conditional)   except they are mentioned in the Implementation Guidelines.**   Therefore the implementer might add these in his own realisation of a comlient API in addition to the elements defined in this file.  ## General Remarks on Data Types  The Berlin Group definition of UTF-8 strings in context of the API have to support at least the following characters  a b c d e f g h i j k l m n o p q r s t u v w x y z  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  0 1 2 3 4 5 6 7 8 9  / - ? : ( ) . , ' +  Space 
 *
 * The version of the OpenAPI document: 1.3.8_2020-12-14 - Swiss edition 1.3.8.1-CH
 * Contact: info@obp.ch
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAI_linksStartScaProcess.h
 *
 * A list of hyperlinks to be recognised by the TPP. The actual hyperlinks used in the response depend on the dynamical decisions of the ASPSP when processing the request.  **Remark:** All links can be relative or full links, to be decided by the ASPSP.  Type of links admitted in this response, (further links might be added for ASPSP defined extensions):  - &#39;scaRedirect&#39;:   In case of an SCA Redirect Approach, the ASPSP is transmitting the link to which to   redirect the PSU browser. - &#39;scaOAuth&#39;:   In case of a SCA OAuth2 Approach, the ASPSP is transmitting the URI where the configuration of the Authorisation Server can be retrieved. The configuration follows the OAuth 2.0 Authorisation Server Metadata specification. * &#39;confirmation&#39;:    Might be added by the ASPSP if either the \&quot;scaRedirect\&quot; or \&quot;scaOAuth\&quot; hyperlink is returned    in the same response message.    This hyperlink defines the URL to the resource which needs to be updated with      * a confirmation code as retrieved after the plain redirect authentication process with the ASPSP authentication server or     * an access token as retrieved by submitting an authorization code after the integrated OAuth based authentication process with the ASPSP authentication server. - &#39;updatePsuIdentification&#39;:    The link to the authorisation or cancellation authorisation sub-resource,    where PSU identification data needs to be uploaded. - &#39;startAuthorisationWithPsuAuthentication&#39;:   The link to the authorisation or cancellation authorisation sub-resource,   where PSU authentication data needs to be uploaded. - &#39;startAuthorisationWithEncryptedPsuAuthentication&#39;:     Same as startAuthorisactionWithPsuAuthentication where the authentication data need to be encrypted on     application layer in uploading. - &#39;selectAuthenticationMethod&#39;:   The link to the authorisation or cancellation authorisation sub-resource,   where the selected authentication method needs to be uploaded.   This link is contained under exactly the same conditions as the data element &#39;scaMethods&#39;. - &#39;authoriseTransaction&#39;:   The link to the authorisation or cancellation authorisation sub-resource,   where the authorisation data has to be uploaded, e.g. the TOP received by SMS. - &#39;scaStatus&#39;:   The link to retrieve the scaStatus of the corresponding authorisation sub-resource. 
 */

#ifndef OAI_linksStartScaProcess_H
#define OAI_linksStartScaProcess_H

#include <QJsonObject>

#include "OAIHrefType.h"
#include <QMap>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIHrefType;

class OAI_linksStartScaProcess : public OAIObject {
public:
    OAI_linksStartScaProcess();
    OAI_linksStartScaProcess(QString json);
    ~OAI_linksStartScaProcess() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIHrefType getAuthoriseTransaction() const;
    void setAuthoriseTransaction(const OAIHrefType &authorise_transaction);
    bool is_authorise_transaction_Set() const;
    bool is_authorise_transaction_Valid() const;

    OAIHrefType getConfirmation() const;
    void setConfirmation(const OAIHrefType &confirmation);
    bool is_confirmation_Set() const;
    bool is_confirmation_Valid() const;

    OAIHrefType getScaOAuth() const;
    void setScaOAuth(const OAIHrefType &sca_o_auth);
    bool is_sca_o_auth_Set() const;
    bool is_sca_o_auth_Valid() const;

    OAIHrefType getScaRedirect() const;
    void setScaRedirect(const OAIHrefType &sca_redirect);
    bool is_sca_redirect_Set() const;
    bool is_sca_redirect_Valid() const;

    OAIHrefType getScaStatus() const;
    void setScaStatus(const OAIHrefType &sca_status);
    bool is_sca_status_Set() const;
    bool is_sca_status_Valid() const;

    OAIHrefType getSelectAuthenticationMethod() const;
    void setSelectAuthenticationMethod(const OAIHrefType &select_authentication_method);
    bool is_select_authentication_method_Set() const;
    bool is_select_authentication_method_Valid() const;

    OAIHrefType getStartAuthorisationWithEncryptedPsuAuthentication() const;
    void setStartAuthorisationWithEncryptedPsuAuthentication(const OAIHrefType &start_authorisation_with_encrypted_psu_authentication);
    bool is_start_authorisation_with_encrypted_psu_authentication_Set() const;
    bool is_start_authorisation_with_encrypted_psu_authentication_Valid() const;

    OAIHrefType getStartAuthorisationWithPsuAuthentication() const;
    void setStartAuthorisationWithPsuAuthentication(const OAIHrefType &start_authorisation_with_psu_authentication);
    bool is_start_authorisation_with_psu_authentication_Set() const;
    bool is_start_authorisation_with_psu_authentication_Valid() const;

    OAIHrefType getUpdatePsuIdentification() const;
    void setUpdatePsuIdentification(const OAIHrefType &update_psu_identification);
    bool is_update_psu_identification_Set() const;
    bool is_update_psu_identification_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIHrefType m_authorise_transaction;
    bool m_authorise_transaction_isSet;
    bool m_authorise_transaction_isValid;

    OAIHrefType m_confirmation;
    bool m_confirmation_isSet;
    bool m_confirmation_isValid;

    OAIHrefType m_sca_o_auth;
    bool m_sca_o_auth_isSet;
    bool m_sca_o_auth_isValid;

    OAIHrefType m_sca_redirect;
    bool m_sca_redirect_isSet;
    bool m_sca_redirect_isValid;

    OAIHrefType m_sca_status;
    bool m_sca_status_isSet;
    bool m_sca_status_isValid;

    OAIHrefType m_select_authentication_method;
    bool m_select_authentication_method_isSet;
    bool m_select_authentication_method_isValid;

    OAIHrefType m_start_authorisation_with_encrypted_psu_authentication;
    bool m_start_authorisation_with_encrypted_psu_authentication_isSet;
    bool m_start_authorisation_with_encrypted_psu_authentication_isValid;

    OAIHrefType m_start_authorisation_with_psu_authentication;
    bool m_start_authorisation_with_psu_authentication_isSet;
    bool m_start_authorisation_with_psu_authentication_isValid;

    OAIHrefType m_update_psu_identification;
    bool m_update_psu_identification_isSet;
    bool m_update_psu_identification_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAI_linksStartScaProcess)

#endif // OAI_linksStartScaProcess_H
