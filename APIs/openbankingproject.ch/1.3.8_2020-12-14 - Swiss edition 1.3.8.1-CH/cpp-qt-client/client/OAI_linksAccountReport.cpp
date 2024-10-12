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

#include "OAI_linksAccountReport.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_linksAccountReport::OAI_linksAccountReport(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_linksAccountReport::OAI_linksAccountReport() {
    this->initializeModel();
}

OAI_linksAccountReport::~OAI_linksAccountReport() {}

void OAI_linksAccountReport::initializeModel() {

    m_account_isSet = false;
    m_account_isValid = false;

    m_first_isSet = false;
    m_first_isValid = false;

    m_last_isSet = false;
    m_last_isValid = false;

    m_next_isSet = false;
    m_next_isValid = false;

    m_previous_isSet = false;
    m_previous_isValid = false;
}

void OAI_linksAccountReport::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_linksAccountReport::fromJsonObject(QJsonObject json) {

    m_account_isValid = ::OpenAPI::fromJsonValue(m_account, json[QString("account")]);
    m_account_isSet = !json[QString("account")].isNull() && m_account_isValid;

    m_first_isValid = ::OpenAPI::fromJsonValue(m_first, json[QString("first")]);
    m_first_isSet = !json[QString("first")].isNull() && m_first_isValid;

    m_last_isValid = ::OpenAPI::fromJsonValue(m_last, json[QString("last")]);
    m_last_isSet = !json[QString("last")].isNull() && m_last_isValid;

    m_next_isValid = ::OpenAPI::fromJsonValue(m_next, json[QString("next")]);
    m_next_isSet = !json[QString("next")].isNull() && m_next_isValid;

    m_previous_isValid = ::OpenAPI::fromJsonValue(m_previous, json[QString("previous")]);
    m_previous_isSet = !json[QString("previous")].isNull() && m_previous_isValid;
}

QString OAI_linksAccountReport::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_linksAccountReport::asJsonObject() const {
    QJsonObject obj;
    if (m_account.isSet()) {
        obj.insert(QString("account"), ::OpenAPI::toJsonValue(m_account));
    }
    if (m_first.isSet()) {
        obj.insert(QString("first"), ::OpenAPI::toJsonValue(m_first));
    }
    if (m_last.isSet()) {
        obj.insert(QString("last"), ::OpenAPI::toJsonValue(m_last));
    }
    if (m_next.isSet()) {
        obj.insert(QString("next"), ::OpenAPI::toJsonValue(m_next));
    }
    if (m_previous.isSet()) {
        obj.insert(QString("previous"), ::OpenAPI::toJsonValue(m_previous));
    }
    return obj;
}

OAIHrefType OAI_linksAccountReport::getAccount() const {
    return m_account;
}
void OAI_linksAccountReport::setAccount(const OAIHrefType &account) {
    m_account = account;
    m_account_isSet = true;
}

bool OAI_linksAccountReport::is_account_Set() const{
    return m_account_isSet;
}

bool OAI_linksAccountReport::is_account_Valid() const{
    return m_account_isValid;
}

OAIHrefType OAI_linksAccountReport::getFirst() const {
    return m_first;
}
void OAI_linksAccountReport::setFirst(const OAIHrefType &first) {
    m_first = first;
    m_first_isSet = true;
}

bool OAI_linksAccountReport::is_first_Set() const{
    return m_first_isSet;
}

bool OAI_linksAccountReport::is_first_Valid() const{
    return m_first_isValid;
}

OAIHrefType OAI_linksAccountReport::getLast() const {
    return m_last;
}
void OAI_linksAccountReport::setLast(const OAIHrefType &last) {
    m_last = last;
    m_last_isSet = true;
}

bool OAI_linksAccountReport::is_last_Set() const{
    return m_last_isSet;
}

bool OAI_linksAccountReport::is_last_Valid() const{
    return m_last_isValid;
}

OAIHrefType OAI_linksAccountReport::getNext() const {
    return m_next;
}
void OAI_linksAccountReport::setNext(const OAIHrefType &next) {
    m_next = next;
    m_next_isSet = true;
}

bool OAI_linksAccountReport::is_next_Set() const{
    return m_next_isSet;
}

bool OAI_linksAccountReport::is_next_Valid() const{
    return m_next_isValid;
}

OAIHrefType OAI_linksAccountReport::getPrevious() const {
    return m_previous;
}
void OAI_linksAccountReport::setPrevious(const OAIHrefType &previous) {
    m_previous = previous;
    m_previous_isSet = true;
}

bool OAI_linksAccountReport::is_previous_Set() const{
    return m_previous_isSet;
}

bool OAI_linksAccountReport::is_previous_Valid() const{
    return m_previous_isValid;
}

bool OAI_linksAccountReport::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_first.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_last.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_next.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_previous.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_linksAccountReport::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_account_isValid && true;
}

} // namespace OpenAPI
