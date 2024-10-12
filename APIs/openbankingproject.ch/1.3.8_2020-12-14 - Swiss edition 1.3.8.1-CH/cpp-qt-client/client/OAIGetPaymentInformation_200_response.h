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
 * OAIGetPaymentInformation_200_response.h
 *
 * 
 */

#ifndef OAIGetPaymentInformation_200_response_H
#define OAIGetPaymentInformation_200_response_H

#include <QJsonObject>

#include "OAIAccountReference16_CH.h"
#include "OAIAddress.h"
#include "OAIAmount.h"
#include "OAIBulkPaymentInitiationWithStatusResponse.h"
#include "OAICreditorAgent7_CH.h"
#include "OAIDayOfExecution.h"
#include "OAIExecutionRule.h"
#include "OAIFrequencyCode.h"
#include "OAIPaymentInitiationBulkElement_json.h"
#include "OAIPaymentInitiationWithStatusResponse.h"
#include "OAIPeriodicPaymentInitiationWithStatusResponse.h"
#include "OAIPurposeCode.h"
#include "OAIRemittanceInformationStructured.h"
#include "OAITransactionStatus.h"
#include <QDate>
#include <QDateTime>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAccountReference16_CH;
class OAIAddress;
class OAICreditorAgent7_CH;
class OAIAmount;
class OAIRemittanceInformationStructured;
class OAIPaymentInitiationBulkElement_json;

class OAIGetPaymentInformation_200_response : public OAIObject {
public:
    OAIGetPaymentInformation_200_response();
    OAIGetPaymentInformation_200_response(QString json);
    ~OAIGetPaymentInformation_200_response() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIAccountReference16_CH getCreditorAccount() const;
    void setCreditorAccount(const OAIAccountReference16_CH &creditor_account);
    bool is_creditor_account_Set() const;
    bool is_creditor_account_Valid() const;

    OAIAddress getCreditorAddress() const;
    void setCreditorAddress(const OAIAddress &creditor_address);
    bool is_creditor_address_Set() const;
    bool is_creditor_address_Valid() const;

    OAICreditorAgent7_CH getCreditorAgent() const;
    void setCreditorAgent(const OAICreditorAgent7_CH &creditor_agent);
    bool is_creditor_agent_Set() const;
    bool is_creditor_agent_Valid() const;

    QString getCreditorName() const;
    void setCreditorName(const QString &creditor_name);
    bool is_creditor_name_Set() const;
    bool is_creditor_name_Valid() const;

    OAIAccountReference16_CH getDebtorAccount() const;
    void setDebtorAccount(const OAIAccountReference16_CH &debtor_account);
    bool is_debtor_account_Set() const;
    bool is_debtor_account_Valid() const;

    QString getEndToEndIdentification() const;
    void setEndToEndIdentification(const QString &end_to_end_identification);
    bool is_end_to_end_identification_Set() const;
    bool is_end_to_end_identification_Valid() const;

    OAIAmount getInstructedAmount() const;
    void setInstructedAmount(const OAIAmount &instructed_amount);
    bool is_instructed_amount_Set() const;
    bool is_instructed_amount_Valid() const;

    OAIPurposeCode getPurposeCode() const;
    void setPurposeCode(const OAIPurposeCode &purpose_code);
    bool is_purpose_code_Set() const;
    bool is_purpose_code_Valid() const;

    OAIRemittanceInformationStructured getRemittanceInformationStructured() const;
    void setRemittanceInformationStructured(const OAIRemittanceInformationStructured &remittance_information_structured);
    bool is_remittance_information_structured_Set() const;
    bool is_remittance_information_structured_Valid() const;

    QString getRemittanceInformationUnstructured() const;
    void setRemittanceInformationUnstructured(const QString &remittance_information_unstructured);
    bool is_remittance_information_unstructured_Set() const;
    bool is_remittance_information_unstructured_Valid() const;

    QList<QString> getRemittanceInformationUnstructuredArray() const;
    void setRemittanceInformationUnstructuredArray(const QList<QString> &remittance_information_unstructured_array);
    bool is_remittance_information_unstructured_array_Set() const;
    bool is_remittance_information_unstructured_array_Valid() const;

    QDate getRequestedExecutionDate() const;
    void setRequestedExecutionDate(const QDate &requested_execution_date);
    bool is_requested_execution_date_Set() const;
    bool is_requested_execution_date_Valid() const;

    QDateTime getRequestedExecutionTime() const;
    void setRequestedExecutionTime(const QDateTime &requested_execution_time);
    bool is_requested_execution_time_Set() const;
    bool is_requested_execution_time_Valid() const;

    OAITransactionStatus getTransactionStatus() const;
    void setTransactionStatus(const OAITransactionStatus &transaction_status);
    bool is_transaction_status_Set() const;
    bool is_transaction_status_Valid() const;

    QString getUltimateCreditor() const;
    void setUltimateCreditor(const QString &ultimate_creditor);
    bool is_ultimate_creditor_Set() const;
    bool is_ultimate_creditor_Valid() const;

    QString getUltimateDebtor() const;
    void setUltimateDebtor(const QString &ultimate_debtor);
    bool is_ultimate_debtor_Set() const;
    bool is_ultimate_debtor_Valid() const;

    OAIDayOfExecution getDayOfExecution() const;
    void setDayOfExecution(const OAIDayOfExecution &day_of_execution);
    bool is_day_of_execution_Set() const;
    bool is_day_of_execution_Valid() const;

    QDate getEndDate() const;
    void setEndDate(const QDate &end_date);
    bool is_end_date_Set() const;
    bool is_end_date_Valid() const;

    OAIExecutionRule getExecutionRule() const;
    void setExecutionRule(const OAIExecutionRule &execution_rule);
    bool is_execution_rule_Set() const;
    bool is_execution_rule_Valid() const;

    OAIFrequencyCode getFrequency() const;
    void setFrequency(const OAIFrequencyCode &frequency);
    bool is_frequency_Set() const;
    bool is_frequency_Valid() const;

    QDate getStartDate() const;
    void setStartDate(const QDate &start_date);
    bool is_start_date_Set() const;
    bool is_start_date_Valid() const;

    QDateTime getAcceptorTransactionDateTime() const;
    void setAcceptorTransactionDateTime(const QDateTime &acceptor_transaction_date_time);
    bool is_acceptor_transaction_date_time_Set() const;
    bool is_acceptor_transaction_date_time_Valid() const;

    bool isBatchBookingPreferred() const;
    void setBatchBookingPreferred(const bool &batch_booking_preferred);
    bool is_batch_booking_preferred_Set() const;
    bool is_batch_booking_preferred_Valid() const;

    QString getPaymentInformationId() const;
    void setPaymentInformationId(const QString &payment_information_id);
    bool is_payment_information_id_Set() const;
    bool is_payment_information_id_Valid() const;

    QList<OAIPaymentInitiationBulkElement_json> getPayments() const;
    void setPayments(const QList<OAIPaymentInitiationBulkElement_json> &payments);
    bool is_payments_Set() const;
    bool is_payments_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIAccountReference16_CH m_creditor_account;
    bool m_creditor_account_isSet;
    bool m_creditor_account_isValid;

    OAIAddress m_creditor_address;
    bool m_creditor_address_isSet;
    bool m_creditor_address_isValid;

    OAICreditorAgent7_CH m_creditor_agent;
    bool m_creditor_agent_isSet;
    bool m_creditor_agent_isValid;

    QString m_creditor_name;
    bool m_creditor_name_isSet;
    bool m_creditor_name_isValid;

    OAIAccountReference16_CH m_debtor_account;
    bool m_debtor_account_isSet;
    bool m_debtor_account_isValid;

    QString m_end_to_end_identification;
    bool m_end_to_end_identification_isSet;
    bool m_end_to_end_identification_isValid;

    OAIAmount m_instructed_amount;
    bool m_instructed_amount_isSet;
    bool m_instructed_amount_isValid;

    OAIPurposeCode m_purpose_code;
    bool m_purpose_code_isSet;
    bool m_purpose_code_isValid;

    OAIRemittanceInformationStructured m_remittance_information_structured;
    bool m_remittance_information_structured_isSet;
    bool m_remittance_information_structured_isValid;

    QString m_remittance_information_unstructured;
    bool m_remittance_information_unstructured_isSet;
    bool m_remittance_information_unstructured_isValid;

    QList<QString> m_remittance_information_unstructured_array;
    bool m_remittance_information_unstructured_array_isSet;
    bool m_remittance_information_unstructured_array_isValid;

    QDate m_requested_execution_date;
    bool m_requested_execution_date_isSet;
    bool m_requested_execution_date_isValid;

    QDateTime m_requested_execution_time;
    bool m_requested_execution_time_isSet;
    bool m_requested_execution_time_isValid;

    OAITransactionStatus m_transaction_status;
    bool m_transaction_status_isSet;
    bool m_transaction_status_isValid;

    QString m_ultimate_creditor;
    bool m_ultimate_creditor_isSet;
    bool m_ultimate_creditor_isValid;

    QString m_ultimate_debtor;
    bool m_ultimate_debtor_isSet;
    bool m_ultimate_debtor_isValid;

    OAIDayOfExecution m_day_of_execution;
    bool m_day_of_execution_isSet;
    bool m_day_of_execution_isValid;

    QDate m_end_date;
    bool m_end_date_isSet;
    bool m_end_date_isValid;

    OAIExecutionRule m_execution_rule;
    bool m_execution_rule_isSet;
    bool m_execution_rule_isValid;

    OAIFrequencyCode m_frequency;
    bool m_frequency_isSet;
    bool m_frequency_isValid;

    QDate m_start_date;
    bool m_start_date_isSet;
    bool m_start_date_isValid;

    QDateTime m_acceptor_transaction_date_time;
    bool m_acceptor_transaction_date_time_isSet;
    bool m_acceptor_transaction_date_time_isValid;

    bool m_batch_booking_preferred;
    bool m_batch_booking_preferred_isSet;
    bool m_batch_booking_preferred_isValid;

    QString m_payment_information_id;
    bool m_payment_information_id_isSet;
    bool m_payment_information_id_isValid;

    QList<OAIPaymentInitiationBulkElement_json> m_payments;
    bool m_payments_isSet;
    bool m_payments_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIGetPaymentInformation_200_response)

#endif // OAIGetPaymentInformation_200_response_H
