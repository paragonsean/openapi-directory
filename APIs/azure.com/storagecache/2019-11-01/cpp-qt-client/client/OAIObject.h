/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage Caches.
 *
 * The version of the OpenAPI document: 2019-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OBJECT_H
#define OAI_OBJECT_H

#include <QJsonDocument>
#include <QJsonObject>
#include <QMetaType>

namespace OpenAPI {

class OAIObject {
public:
    OAIObject() {}

    OAIObject(QString jsonString) {
        fromJson(jsonString);
    }

    virtual ~OAIObject() {}

    virtual QJsonObject asJsonObject() const {
        return jObj;
    }

    virtual QString asJson() const {
        QJsonDocument doc(jObj);
        return doc.toJson(QJsonDocument::Compact);
    }

    virtual void fromJson(QString jsonString) {
        QJsonDocument doc = QJsonDocument::fromJson(jsonString.toUtf8());
        jObj = doc.object();
    }

    virtual void fromJsonObject(QJsonObject json) {
        jObj = json;
    }

    virtual bool isSet() const {
        return false;
    }

    virtual bool isValid() const {
        return true;
    }

private:
    QJsonObject jObj;
};

inline bool operator==(const OAIObject& left, const OAIObject& right){  
    return (left.asJsonObject() == right.asJsonObject());  
}

inline
#if QT_VERSION < 0x060000
uint
#else
size_t
#endif
qHash(const OAIObject& obj, uint seed = 0) noexcept{
    return qHash(obj.asJsonObject(), seed);
}

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIObject)

#endif // OAI_OBJECT_H
