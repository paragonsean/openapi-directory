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

#include "OAIError401_NG_AIS.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIError401_NG_AIS::OAIError401_NG_AIS(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIError401_NG_AIS::OAIError401_NG_AIS() {
    this->initializeModel();
}

OAIError401_NG_AIS::~OAIError401_NG_AIS() {}

void OAIError401_NG_AIS::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_tpp_messages_isSet = false;
    m_tpp_messages_isValid = false;
}

void OAIError401_NG_AIS::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIError401_NG_AIS::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_tpp_messages_isValid = ::OpenAPI::fromJsonValue(m_tpp_messages, json[QString("tppMessages")]);
    m_tpp_messages_isSet = !json[QString("tppMessages")].isNull() && m_tpp_messages_isValid;
}

QString OAIError401_NG_AIS::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIError401_NG_AIS::asJsonObject() const {
    QJsonObject obj;
    if (m__links.isSet()) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_tpp_messages.size() > 0) {
        obj.insert(QString("tppMessages"), ::OpenAPI::toJsonValue(m_tpp_messages));
    }
    return obj;
}

OAI_linksAll OAIError401_NG_AIS::getLinks() const {
    return m__links;
}
void OAIError401_NG_AIS::setLinks(const OAI_linksAll &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIError401_NG_AIS::is__links_Set() const{
    return m__links_isSet;
}

bool OAIError401_NG_AIS::is__links_Valid() const{
    return m__links_isValid;
}

QList<OAITppMessage401_AIS> OAIError401_NG_AIS::getTppMessages() const {
    return m_tpp_messages;
}
void OAIError401_NG_AIS::setTppMessages(const QList<OAITppMessage401_AIS> &tpp_messages) {
    m_tpp_messages = tpp_messages;
    m_tpp_messages_isSet = true;
}

bool OAIError401_NG_AIS::is_tpp_messages_Set() const{
    return m_tpp_messages_isSet;
}

bool OAIError401_NG_AIS::is_tpp_messages_Valid() const{
    return m_tpp_messages_isValid;
}

bool OAIError401_NG_AIS::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_tpp_messages.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIError401_NG_AIS::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
