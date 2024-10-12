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

#include "OAI_linksUpdatePsuIdentification.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_linksUpdatePsuIdentification::OAI_linksUpdatePsuIdentification(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_linksUpdatePsuIdentification::OAI_linksUpdatePsuIdentification() {
    this->initializeModel();
}

OAI_linksUpdatePsuIdentification::~OAI_linksUpdatePsuIdentification() {}

void OAI_linksUpdatePsuIdentification::initializeModel() {

    m_sca_status_isSet = false;
    m_sca_status_isValid = false;

    m_select_authentication_method_isSet = false;
    m_select_authentication_method_isValid = false;
}

void OAI_linksUpdatePsuIdentification::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_linksUpdatePsuIdentification::fromJsonObject(QJsonObject json) {

    m_sca_status_isValid = ::OpenAPI::fromJsonValue(m_sca_status, json[QString("scaStatus")]);
    m_sca_status_isSet = !json[QString("scaStatus")].isNull() && m_sca_status_isValid;

    m_select_authentication_method_isValid = ::OpenAPI::fromJsonValue(m_select_authentication_method, json[QString("selectAuthenticationMethod")]);
    m_select_authentication_method_isSet = !json[QString("selectAuthenticationMethod")].isNull() && m_select_authentication_method_isValid;
}

QString OAI_linksUpdatePsuIdentification::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_linksUpdatePsuIdentification::asJsonObject() const {
    QJsonObject obj;
    if (m_sca_status.isSet()) {
        obj.insert(QString("scaStatus"), ::OpenAPI::toJsonValue(m_sca_status));
    }
    if (m_select_authentication_method.isSet()) {
        obj.insert(QString("selectAuthenticationMethod"), ::OpenAPI::toJsonValue(m_select_authentication_method));
    }
    return obj;
}

OAIHrefType OAI_linksUpdatePsuIdentification::getScaStatus() const {
    return m_sca_status;
}
void OAI_linksUpdatePsuIdentification::setScaStatus(const OAIHrefType &sca_status) {
    m_sca_status = sca_status;
    m_sca_status_isSet = true;
}

bool OAI_linksUpdatePsuIdentification::is_sca_status_Set() const{
    return m_sca_status_isSet;
}

bool OAI_linksUpdatePsuIdentification::is_sca_status_Valid() const{
    return m_sca_status_isValid;
}

OAIHrefType OAI_linksUpdatePsuIdentification::getSelectAuthenticationMethod() const {
    return m_select_authentication_method;
}
void OAI_linksUpdatePsuIdentification::setSelectAuthenticationMethod(const OAIHrefType &select_authentication_method) {
    m_select_authentication_method = select_authentication_method;
    m_select_authentication_method_isSet = true;
}

bool OAI_linksUpdatePsuIdentification::is_select_authentication_method_Set() const{
    return m_select_authentication_method_isSet;
}

bool OAI_linksUpdatePsuIdentification::is_select_authentication_method_Valid() const{
    return m_select_authentication_method_isValid;
}

bool OAI_linksUpdatePsuIdentification::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_sca_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_select_authentication_method.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_linksUpdatePsuIdentification::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
