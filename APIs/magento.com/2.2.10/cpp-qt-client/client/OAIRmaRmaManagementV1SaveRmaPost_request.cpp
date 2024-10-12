/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRmaRmaManagementV1SaveRmaPost_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRmaRmaManagementV1SaveRmaPost_request::OAIRmaRmaManagementV1SaveRmaPost_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRmaRmaManagementV1SaveRmaPost_request::OAIRmaRmaManagementV1SaveRmaPost_request() {
    this->initializeModel();
}

OAIRmaRmaManagementV1SaveRmaPost_request::~OAIRmaRmaManagementV1SaveRmaPost_request() {}

void OAIRmaRmaManagementV1SaveRmaPost_request::initializeModel() {

    m_rma_data_object_isSet = false;
    m_rma_data_object_isValid = false;
}

void OAIRmaRmaManagementV1SaveRmaPost_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRmaRmaManagementV1SaveRmaPost_request::fromJsonObject(QJsonObject json) {

    m_rma_data_object_isValid = ::OpenAPI::fromJsonValue(m_rma_data_object, json[QString("rmaDataObject")]);
    m_rma_data_object_isSet = !json[QString("rmaDataObject")].isNull() && m_rma_data_object_isValid;
}

QString OAIRmaRmaManagementV1SaveRmaPost_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRmaRmaManagementV1SaveRmaPost_request::asJsonObject() const {
    QJsonObject obj;
    if (m_rma_data_object.isSet()) {
        obj.insert(QString("rmaDataObject"), ::OpenAPI::toJsonValue(m_rma_data_object));
    }
    return obj;
}

OAIRma_data_rma_interface OAIRmaRmaManagementV1SaveRmaPost_request::getRmaDataObject() const {
    return m_rma_data_object;
}
void OAIRmaRmaManagementV1SaveRmaPost_request::setRmaDataObject(const OAIRma_data_rma_interface &rma_data_object) {
    m_rma_data_object = rma_data_object;
    m_rma_data_object_isSet = true;
}

bool OAIRmaRmaManagementV1SaveRmaPost_request::is_rma_data_object_Set() const{
    return m_rma_data_object_isSet;
}

bool OAIRmaRmaManagementV1SaveRmaPost_request::is_rma_data_object_Valid() const{
    return m_rma_data_object_isValid;
}

bool OAIRmaRmaManagementV1SaveRmaPost_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_rma_data_object.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRmaRmaManagementV1SaveRmaPost_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_rma_data_object_isValid && true;
}

} // namespace OpenAPI
