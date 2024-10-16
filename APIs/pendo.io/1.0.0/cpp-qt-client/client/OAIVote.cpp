/**
 * Pendo Feedback API
 * ## Who is this for?  This documentation is for developers creating their own integration with [Feedback's](https://www.pendo.io/product/feedback/) API. If you are doing a standard integration, there's a really easy [Javascript integration](https://help.receptive.io/hc/en-us/articles/209221969-How-to-integrate-Receptive-with-your-app) that you should know about before you go to the effort of building your own integration.  ## Authentication  API calls generally need to be authenticated. Generate an API Key at https://feedback.pendo.io/app/#/vendor/settings?section=integrate. This key should then be added to every request as a request header named 'auth-token' (preferred), or as a query parameter named 'auth-token'.  ## Endpoint  API endpoint is https://api.feedback.eu.pendo.io / https://api.feedback.us.pendo.io depending where your datacenter is located.  ## Notes  API endpoints are being added to this documentation as needed by customers. If you don't see an endpoint you need please contact support and if it exists we'll publish the docs here. The 'try it out' feature on this documentation page will probably be blocked by your browser because the Access-Control-Allow-Origin header has its value set by the Feedback server depending on your hostname.  ## Generating client code  This documentation is automatically generated from an OpenAPI spec available [here](http://apidoc.receptive.io/receptive.swagger.json). You can use Swagger to auto-generate API client code in many languages using the [Swagger Editor](http://editor.swagger.io/#/)
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@receptive.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIVote.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIVote::OAIVote(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIVote::OAIVote() {
    this->initializeModel();
}

OAIVote::~OAIVote() {}

void OAIVote::initializeModel() {

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_feature_id_isSet = false;
    m_feature_id_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;

    m_user_id_isSet = false;
    m_user_id_isValid = false;
}

void OAIVote::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIVote::fromJsonObject(QJsonObject json) {

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_feature_id_isValid = ::OpenAPI::fromJsonValue(m_feature_id, json[QString("feature_id")]);
    m_feature_id_isSet = !json[QString("feature_id")].isNull() && m_feature_id_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;

    m_user_id_isValid = ::OpenAPI::fromJsonValue(m_user_id, json[QString("user_id")]);
    m_user_id_isSet = !json[QString("user_id")].isNull() && m_user_id_isValid;
}

QString OAIVote::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIVote::asJsonObject() const {
    QJsonObject obj;
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_feature_id_isSet) {
        obj.insert(QString("feature_id"), ::OpenAPI::toJsonValue(m_feature_id));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    if (m_user_id_isSet) {
        obj.insert(QString("user_id"), ::OpenAPI::toJsonValue(m_user_id));
    }
    return obj;
}

QString OAIVote::getCreatedAt() const {
    return m_created_at;
}
void OAIVote::setCreatedAt(const QString &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIVote::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIVote::is_created_at_Valid() const{
    return m_created_at_isValid;
}

qint32 OAIVote::getFeatureId() const {
    return m_feature_id;
}
void OAIVote::setFeatureId(const qint32 &feature_id) {
    m_feature_id = feature_id;
    m_feature_id_isSet = true;
}

bool OAIVote::is_feature_id_Set() const{
    return m_feature_id_isSet;
}

bool OAIVote::is_feature_id_Valid() const{
    return m_feature_id_isValid;
}

qint32 OAIVote::getQuantity() const {
    return m_quantity;
}
void OAIVote::setQuantity(const qint32 &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAIVote::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAIVote::is_quantity_Valid() const{
    return m_quantity_isValid;
}

QString OAIVote::getUpdatedAt() const {
    return m_updated_at;
}
void OAIVote::setUpdatedAt(const QString &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIVote::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIVote::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

qint32 OAIVote::getUserId() const {
    return m_user_id;
}
void OAIVote::setUserId(const qint32 &user_id) {
    m_user_id = user_id;
    m_user_id_isSet = true;
}

bool OAIVote::is_user_id_Set() const{
    return m_user_id_isSet;
}

bool OAIVote::is_user_id_Valid() const{
    return m_user_id_isValid;
}

bool OAIVote::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_feature_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIVote::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
