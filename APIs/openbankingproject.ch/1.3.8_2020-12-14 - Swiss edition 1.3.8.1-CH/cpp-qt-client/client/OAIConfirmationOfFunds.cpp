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

#include "OAIConfirmationOfFunds.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConfirmationOfFunds::OAIConfirmationOfFunds(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConfirmationOfFunds::OAIConfirmationOfFunds() {
    this->initializeModel();
}

OAIConfirmationOfFunds::~OAIConfirmationOfFunds() {}

void OAIConfirmationOfFunds::initializeModel() {

    m_account_isSet = false;
    m_account_isValid = false;

    m_card_number_isSet = false;
    m_card_number_isValid = false;

    m_instructed_amount_isSet = false;
    m_instructed_amount_isValid = false;

    m_payee_isSet = false;
    m_payee_isValid = false;
}

void OAIConfirmationOfFunds::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConfirmationOfFunds::fromJsonObject(QJsonObject json) {

    m_account_isValid = ::OpenAPI::fromJsonValue(m_account, json[QString("account")]);
    m_account_isSet = !json[QString("account")].isNull() && m_account_isValid;

    m_card_number_isValid = ::OpenAPI::fromJsonValue(m_card_number, json[QString("cardNumber")]);
    m_card_number_isSet = !json[QString("cardNumber")].isNull() && m_card_number_isValid;

    m_instructed_amount_isValid = ::OpenAPI::fromJsonValue(m_instructed_amount, json[QString("instructedAmount")]);
    m_instructed_amount_isSet = !json[QString("instructedAmount")].isNull() && m_instructed_amount_isValid;

    m_payee_isValid = ::OpenAPI::fromJsonValue(m_payee, json[QString("payee")]);
    m_payee_isSet = !json[QString("payee")].isNull() && m_payee_isValid;
}

QString OAIConfirmationOfFunds::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConfirmationOfFunds::asJsonObject() const {
    QJsonObject obj;
    if (m_account.isSet()) {
        obj.insert(QString("account"), ::OpenAPI::toJsonValue(m_account));
    }
    if (m_card_number_isSet) {
        obj.insert(QString("cardNumber"), ::OpenAPI::toJsonValue(m_card_number));
    }
    if (m_instructed_amount.isSet()) {
        obj.insert(QString("instructedAmount"), ::OpenAPI::toJsonValue(m_instructed_amount));
    }
    if (m_payee_isSet) {
        obj.insert(QString("payee"), ::OpenAPI::toJsonValue(m_payee));
    }
    return obj;
}

OAIAccountReference16_CH OAIConfirmationOfFunds::getAccount() const {
    return m_account;
}
void OAIConfirmationOfFunds::setAccount(const OAIAccountReference16_CH &account) {
    m_account = account;
    m_account_isSet = true;
}

bool OAIConfirmationOfFunds::is_account_Set() const{
    return m_account_isSet;
}

bool OAIConfirmationOfFunds::is_account_Valid() const{
    return m_account_isValid;
}

QString OAIConfirmationOfFunds::getCardNumber() const {
    return m_card_number;
}
void OAIConfirmationOfFunds::setCardNumber(const QString &card_number) {
    m_card_number = card_number;
    m_card_number_isSet = true;
}

bool OAIConfirmationOfFunds::is_card_number_Set() const{
    return m_card_number_isSet;
}

bool OAIConfirmationOfFunds::is_card_number_Valid() const{
    return m_card_number_isValid;
}

OAIAmount OAIConfirmationOfFunds::getInstructedAmount() const {
    return m_instructed_amount;
}
void OAIConfirmationOfFunds::setInstructedAmount(const OAIAmount &instructed_amount) {
    m_instructed_amount = instructed_amount;
    m_instructed_amount_isSet = true;
}

bool OAIConfirmationOfFunds::is_instructed_amount_Set() const{
    return m_instructed_amount_isSet;
}

bool OAIConfirmationOfFunds::is_instructed_amount_Valid() const{
    return m_instructed_amount_isValid;
}

QString OAIConfirmationOfFunds::getPayee() const {
    return m_payee;
}
void OAIConfirmationOfFunds::setPayee(const QString &payee) {
    m_payee = payee;
    m_payee_isSet = true;
}

bool OAIConfirmationOfFunds::is_payee_Set() const{
    return m_payee_isSet;
}

bool OAIConfirmationOfFunds::is_payee_Valid() const{
    return m_payee_isValid;
}

bool OAIConfirmationOfFunds::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_card_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_instructed_amount.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_payee_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConfirmationOfFunds::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_account_isValid && m_instructed_amount_isValid && true;
}

} // namespace OpenAPI
