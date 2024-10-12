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
 * OAIUpdatePsuIdenticationResponse.h
 *
 * Body of the JSON response for a successful update PSU identification request.
 */

#ifndef OAIUpdatePsuIdenticationResponse_H
#define OAIUpdatePsuIdenticationResponse_H

#include <QJsonObject>

#include "OAIAmount.h"
#include "OAIAuthenticationObject.h"
#include "OAIScaStatus.h"
#include "OAI_linksUpdatePsuIdentification.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAmount;
class OAIAuthenticationObject;

class OAIUpdatePsuIdenticationResponse : public OAIObject {
public:
    OAIUpdatePsuIdenticationResponse();
    OAIUpdatePsuIdenticationResponse(QString json);
    ~OAIUpdatePsuIdenticationResponse() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAI_linksUpdatePsuIdentification getLinks() const;
    void setLinks(const OAI_linksUpdatePsuIdentification &_links);
    bool is__links_Set() const;
    bool is__links_Valid() const;

    OAIAmount getCurrencyConversionFees() const;
    void setCurrencyConversionFees(const OAIAmount &currency_conversion_fees);
    bool is_currency_conversion_fees_Set() const;
    bool is_currency_conversion_fees_Valid() const;

    OAIAmount getEstimatedInterbankSettlementAmount() const;
    void setEstimatedInterbankSettlementAmount(const OAIAmount &estimated_interbank_settlement_amount);
    bool is_estimated_interbank_settlement_amount_Set() const;
    bool is_estimated_interbank_settlement_amount_Valid() const;

    OAIAmount getEstimatedTotalAmount() const;
    void setEstimatedTotalAmount(const OAIAmount &estimated_total_amount);
    bool is_estimated_total_amount_Set() const;
    bool is_estimated_total_amount_Valid() const;

    QString getPsuMessage() const;
    void setPsuMessage(const QString &psu_message);
    bool is_psu_message_Set() const;
    bool is_psu_message_Valid() const;

    QList<OAIAuthenticationObject> getScaMethods() const;
    void setScaMethods(const QList<OAIAuthenticationObject> &sca_methods);
    bool is_sca_methods_Set() const;
    bool is_sca_methods_Valid() const;

    OAIScaStatus getScaStatus() const;
    void setScaStatus(const OAIScaStatus &sca_status);
    bool is_sca_status_Set() const;
    bool is_sca_status_Valid() const;

    OAIAmount getTransactionFees() const;
    void setTransactionFees(const OAIAmount &transaction_fees);
    bool is_transaction_fees_Set() const;
    bool is_transaction_fees_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAI_linksUpdatePsuIdentification m__links;
    bool m__links_isSet;
    bool m__links_isValid;

    OAIAmount m_currency_conversion_fees;
    bool m_currency_conversion_fees_isSet;
    bool m_currency_conversion_fees_isValid;

    OAIAmount m_estimated_interbank_settlement_amount;
    bool m_estimated_interbank_settlement_amount_isSet;
    bool m_estimated_interbank_settlement_amount_isValid;

    OAIAmount m_estimated_total_amount;
    bool m_estimated_total_amount_isSet;
    bool m_estimated_total_amount_isValid;

    QString m_psu_message;
    bool m_psu_message_isSet;
    bool m_psu_message_isValid;

    QList<OAIAuthenticationObject> m_sca_methods;
    bool m_sca_methods_isSet;
    bool m_sca_methods_isValid;

    OAIScaStatus m_sca_status;
    bool m_sca_status_isSet;
    bool m_sca_status_isValid;

    OAIAmount m_transaction_fees;
    bool m_transaction_fees_isSet;
    bool m_transaction_fees_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIUpdatePsuIdenticationResponse)

#endif // OAIUpdatePsuIdenticationResponse_H
